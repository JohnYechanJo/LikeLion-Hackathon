from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from .serializers import LoginSerializer, SignUpStep1Serializer, SignUpStep2Serializer, SignUpStep3Serializer, SignUpStep4Serializer
from django.contrib.auth.models import User
from .models import Profile
from decimal import Decimal
from .forms import SignUpFormStep1, SignUpFormStep2, SignUpFormStep3, SignUpFormStep4

class LoginView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('home')  # 로그인 성공 후 홈 페이지로 리디렉션
        return render(request, 'login.html', {'form': serializer})
    
class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        logout(request)
        return redirect('user_login')  # 로그아웃 후 로그인 페이지로 리디렉션
    def get(self, request):
        logout(request)
        return redirect('user_login')  # 로그아웃 후 로그인 페이지로 리디렉션

class SignUpStep1View(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = SignUpFormStep1()
        return render(request, 'signup1.html', {'form': form})

    def post(self, request):
        form = SignUpFormStep1(request.POST)
        if form.is_valid():
            request.session['signup_data'] = form.cleaned_data
            return redirect('signup_step2')
        return render(request, 'signup1.html', {'form': form})

class SignUpStep2View(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = SignUpFormStep2()
        return render(request, 'signup2.html', {'form': form})

    def post(self, request):
        form = SignUpFormStep2(request.POST)
        if form.is_valid():
            data = request.session.get('signup_data', {})
            data.update(form.cleaned_data)
            request.session['signup_data'] = data
            return redirect('signup_step3')
        return render(request, 'signup2.html', {'form': form})

class SignUpStep3View(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = SignUpFormStep3()
        return render(request, 'signup3.html', {'form': form})

    def post(self, request):
        form = SignUpFormStep3(request.POST)
        if form.is_valid():
            data = request.session.get('signup_data', {})
            cleaned_data = form.cleaned_data
            for key in ['height', 'weight']:
                if key in cleaned_data:
                    cleaned_data[key] = str(cleaned_data[key])
            data.update(cleaned_data)
            request.session['signup_data'] = data
            return redirect('signup_step4')
        return render(request, 'signup3.html', {'form': form})

class SignUpStep4View(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = SignUpFormStep4()
        return render(request, 'signup4.html', {'form': form})

    def post(self, request):
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
                form.add_error(None, str(e))
        return render(request, 'signup4.html', {'form': form})
    
class MyCalorieView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'mycalorie.html')
        else:
            return redirect('user_login')