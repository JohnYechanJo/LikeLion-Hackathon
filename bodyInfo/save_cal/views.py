from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, FoodCal, ExerciseCal, UserCal
from django.db.models import Sum, F
from django.utils import timezone
from account.models import Profile
import pytz

@login_required
def profile_view(request):
    # 로그인한 사용자 정보를 가져옵니다.
    user = request.user
    # 해당 사용자의 프로필 정보를 가져옵니다.
    profile = Profile.objects.get(user=user)
    
    height = float(profile.height)
    weight = float(profile.weight)
    gender = profile.gender
    age_group = profile.age
    exercise_frequency = profile.exercise_frequency

    # 체지방률 계산 (간단한 공식을 사용)
    if gender == 'M':
        body_fat_percentage = 1.20 * (weight / ((height / 100) ** 2)) + 0.23 * 25 - 16.2
        if age_group < 19:
            body_fat_percentage -= 4
    else:
        body_fat_percentage = 1.20 * (weight / ((height / 100) ** 2)) + 0.23 * 25 - 5.4
        if age_group < 19:
            body_fat_percentage -= 4

            # 기초 대사량(BMR) 계산
    if gender == 'M':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * 25)
    else:
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * 25)

    # 총 칼로리 요구량(TDEE) 계산
    if exercise_frequency == 0:
        TDEE = BMR * 1.2
    elif exercise_frequency <= 3:
        TDEE = BMR * 1.375
    elif exercise_frequency <= 5:
        TDEE = BMR * 1.55
    else:
        TDEE = BMR * 1.725

    context = {
        'user': user,
        'profile': profile,
        'body_fat_percentage': body_fat_percentage,
        'BMR': BMR,
        'TDEE': TDEE,
    }

    return render(request, 'profile.html', context)

@login_required
def calorie_input_view(request):
    if request.method == 'POST':
        food_items = request.POST.getlist('food_items')
        exercise_items = request.POST.getlist('exercise_items')

        # 음식 칼로리 데이터 초기화
        food_data = {
            'hamberger': 0,
            'pizza': 0,
            'chicken': 0,
        }

        # 운동 칼로리 데이터 초기화
        exercise_data = {
            'walk': 0,
            'run': 0,
            'weight_training': 0,
        }

        # FoodCal 객체 생성
        food_cal = FoodCal.objects.get()
        exercise_cal = ExerciseCal.objects.get()


        food_data = {
            'hamberger': food_cal.hamberger if 'hamberger' in food_items else 0,
            'pizza': food_cal.pizza if 'pizza' in food_items else 0,
            'chicken': food_cal.chicken if 'chicken' in food_items else 0,
        }

        # 운동 칼로리 계산
        exercise_data = {
            'walk': exercise_cal.walk if 'walk' in exercise_items else 0,
            'run': exercise_cal.run if 'run' in exercise_items else 0,
            'weight_training': exercise_cal.weight_training if 'weight_training' in exercise_items else 0,
        }
        # 한국 시간대 설정
        korea_tz = pytz.timezone('Asia/Seoul')

        # 현재 한국 시간 기준으로 오늘 날짜 가져오기
        today_korea = timezone.now().astimezone(korea_tz).date()
        user_cal = UserCal(
            user=request.user,
            date=today_korea,
            hamberger=food_data["hamberger"],
            pizza=food_data["pizza"],
            chicken=food_data["chicken"],
            walk=exercise_data["walk"],
            run=exercise_data["run"],
            weight_training=exercise_data["weight_training"]
        )
        user_cal.save()
        user_records = UserCal.objects.filter(user=request.user).values('date').annotate(
            total_hamberger=Sum('hamberger'),
            total_pizza=Sum('pizza'),
            total_chicken=Sum('chicken'),
            total_walk=Sum('walk'),
            total_run=Sum('run'),
            total_weight_training=Sum('weight_training'),
            foodcal=Sum(F('hamberger') + F('pizza') + F('chicken')),
            exercal=Sum(F('walk') + F('run') + F('weight_training')),
        ).order_by('date')

        record = {
            'user_records': user_records,
        }
        return render(request, 'calorie_output.html', record)
        
    return render(request, 'calorie_input.html')

def calorie_output_view(request):
    # 날짜별 집계
    user_records = UserCal.objects.filter(user=request.user).values('date').annotate(
        total_hamberger=Sum('hamberger'),
        total_pizza=Sum('pizza'),
        total_chicken=Sum('chicken'),
        total_walk=Sum('walk'),
        total_run=Sum('run'),
        total_weight_training=Sum('weight_training'),
        foodcal=Sum(F('hamberger') + F('pizza') + F('chicken')),
        exercal=Sum(F('walk') + F('run') + F('weight_training')),
    ).order_by('date')

    record = {
        'user_records': user_records,
    }
    return render(request, 'calorie_output.html', record)

def foodcal_output_view(request):
    # 날짜별 집계
    user_records = UserCal.objects.filter(user=request.user).values('date').annotate(
        total_hamberger=Sum('hamberger'),
        total_pizza=Sum('pizza'),
        total_chicken=Sum('chicken'),
        foodcal=Sum(F('hamberger') + F('pizza') + F('chicken')),
    ).order_by('date')

    # 로그인한 사용자 정보를 가져옵니다.
    user = request.user
    # 해당 사용자의 프로필 정보를 가져옵니다.
    profile = Profile.objects.get(user=user)
    height = float(profile.height)
    weight = float(profile.weight)
    gender = profile.gender
    exercise_frequency = profile.exercise_frequency

    # 기초 대사량(BMR) 계산
    if gender == 'M':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * 25)
    else:
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * 25)

    # 총 칼로리 요구량(TDEE) 계산
    if exercise_frequency == 0:
        TDEE = BMR * 1.2
    elif exercise_frequency <= 3:
        TDEE = BMR * 1.375
    elif exercise_frequency <= 5:
        TDEE = BMR * 1.55
    else:
        TDEE = BMR * 1.725

    record = {
        'user_records': user_records,
        'TDEE': TDEE
    }
    
    return render(request, 'foodcal.html', record)

def exercal_output_view(request):
    # 날짜별 집계
    user_records = UserCal.objects.filter(user=request.user).values('date').annotate(
        total_walk=Sum('walk'),
        total_run=Sum('run'),
        total_weight_training=Sum('weight_training'),
        exercal=Sum(F('walk') + F('run') + F('weight_training')),
    ).order_by('date')
    
    user = request.user
    # 해당 사용자의 프로필 정보를 가져옵니다.
    profile = Profile.objects.get(user=user)
    height = float(profile.height)
    weight = float(profile.weight)
    gender = profile.gender
    exercise_frequency = profile.exercise_frequency

    # 기초 대사량(BMR) 계산
    if gender == 'M':
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * 25)
    else:
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * 25)

    # 총 칼로리 요구량(TDEE) 계산
    if exercise_frequency == 0:
        TDEE = BMR * 1.2
    elif exercise_frequency <= 3:
        TDEE = BMR * 1.375
    elif exercise_frequency <= 5:
        TDEE = BMR * 1.55
    else:
        TDEE = BMR * 1.725

    record = {
        'user_records': user_records,
        'TDEE': TDEE
    }
    
    return render(request, 'exercal.html', record)