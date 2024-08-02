from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User
from .models import Profile
from django.db import transaction
from .forms import LoginForm, SignUpFormStep1, SignUpFormStep2, SignUpFormStep3, SignUpFormStep4
from decimal import Decimal

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')


def signup_step1(request):
    if request.method == 'POST':
        form = SignUpFormStep1(request.POST)
        if form.is_valid():
            request.session['signup_data'] = form.cleaned_data
            return redirect('signup_step2')
    else:
        form = SignUpFormStep1()
    return render(request, 'signup1.html', {'form': form})

def signup_step2(request):
    if request.method == 'POST':
        form = SignUpFormStep2(request.POST)
        if form.is_valid():
            data = request.session.get('signup_data', {})
            data.update(form.cleaned_data)
            request.session['signup_data'] = data
            return redirect('signup_step3')
    else:
        initial_data = request.session.get('signup_data', {})
        form = SignUpFormStep2(initial=initial_data)
    return render(request, 'signup2.html', {'form': form})

def signup_step3(request):
    if request.method == 'POST':
        form = SignUpFormStep3(request.POST)
        if form.is_valid():
            data = request.session.get('signup_data', {})
            cleaned_data = form.cleaned_data

            # Convert Decimal fields to string
            for key in ['height', 'weight']:
                if key in cleaned_data:
                    cleaned_data[key] = str(cleaned_data[key])
            
            data.update(cleaned_data)
            request.session['signup_data'] = data
            return redirect('signup_step4')
    else:
        initial_data = request.session.get('signup_data', {})
        # Convert string fields back to Decimal
        if 'height' in initial_data:
            initial_data['height'] = Decimal(initial_data['height'])
        if 'weight' in initial_data:
            initial_data['weight'] = Decimal(initial_data['weight'])
        form = SignUpFormStep3(initial=initial_data)

    return render(request, 'signup3.html', {'form': form})

def signup_step4(request):
    if request.method == 'POST':
        form = SignUpFormStep4(request.POST)
        if form.is_valid():
            data = request.session.get('signup_data', {})
            data.update(form.cleaned_data)
            try:
                user = User.objects.create_user(
                    username=data['username'],
                    password=data['password'],  
                )
                Profile.objects.create(
                    user=user,
                    nickname=data['nickname'],
                    email=data['email'],
                    phone_number=data['phone_number'],
                    gender=data['gender'],
                    age=data['age'],
                    height=data['height'],
                    weight=data['weight'],
                    exercise_frequency=data['exercise_frequency']
                )
                new_user = authenticate(username=data['username'], password=data['password'])
                if new_user is not None:
                    login(request, new_user)
                    request.session.pop('signup_data', None)
                    return redirect('home')
            except Exception as e:
                # 로그 또는 오류 처리
                form.add_error(None, str(e))
    else:
        initial_data = request.session.get('signup_data', {})
        form = SignUpFormStep4(initial=initial_data)
    return render(request, 'signup4.html', {'form': form})


def mycalorie(request):
    return render(request, 'mycalorie.html')