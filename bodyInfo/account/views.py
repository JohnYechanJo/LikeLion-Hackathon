from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from .models import Profile

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # 추가 필드(Profile 모델) 저장
            profile = Profile(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                exercise_frequency=form.cleaned_data['exercise_frequency']
            )
            profile.save()

            # 사용자 인증 및 로그인
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if new_user is not None:
                login(request, new_user)
                return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})