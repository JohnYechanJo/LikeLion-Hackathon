from django.shortcuts import render, redirect, get_object_or_404
from account.models import Profile
from .forms import UserProfileForm

def home(request):
    user = request.user
    
    # 로그인하지 않은 경우, 로그인 페이지로 리다이렉트
    if user.is_anonymous:
        return redirect('user_login')

    # 해당 사용자의 프로필 정보를 가져오기
    profile = get_object_or_404(Profile, user=user)

    # 템플릿에 전달할 컨텍스트 생성
    context = {
        'profile': profile,
    }
    
    return render(request, 'home.html', context)

def calculate_metrics(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            height = profile.height
            weight = profile.weight
            gender = profile.gender
            age_group = profile.age_group
            exercise_frequency = profile.exercise_frequency

            # 체지방률 계산 (간단한 공식을 사용)
            if gender == 'M':
                body_fat_percentage = 1.20 * (weight / ((height / 100) ** 2)) + 0.23 * 25 - 16.2
                if age_group == 'Teen':
                    body_fat_percentage -= 4
            else:
                body_fat_percentage = 1.20 * (weight / ((height / 100) ** 2)) + 0.23 * 25 - 5.4
                if age_group == 'Teen':
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
                'form': form,
                'body_fat_percentage': body_fat_percentage,
                'BMR': BMR,
                'TDEE': TDEE,
            }
            return render(request, 'results.html', context)
    else:
        form = UserProfileForm()
    return render(request, 'calculate.html', {'form': form})