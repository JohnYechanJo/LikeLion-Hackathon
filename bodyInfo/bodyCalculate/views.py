from django.shortcuts import render
from .forms import UserProfileForm

def home(request):
    return render(request, 'home.html')

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