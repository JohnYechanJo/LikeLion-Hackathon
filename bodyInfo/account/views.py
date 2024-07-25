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

            # 사용자 저장
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 패스워드 암호화
            user.save()
            
            # 프로필 생성 및 저장
            Profile.objects.create(user=user)
            
            # 로그인 후 리다이렉트
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})