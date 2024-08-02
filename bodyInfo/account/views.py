# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer, SignUpStep1Serializer, SignUpStep2Serializer, SignUpStep3Serializer, SignUpStep4Serializer
from decimal import Decimal

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SignUpViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def step1(self, request):
        serializer = SignUpStep1Serializer(data=request.data)
        if serializer.is_valid():
            request.session['signup_data'] = serializer.validated_data
            return Response({'message': 'Proceed to step 2'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def step2(self, request):
        serializer = SignUpStep2Serializer(data=request.data)
        if serializer.is_valid():
            request.session['signup_data'].update(serializer.validated_data)
            return Response({'message': 'Proceed to step 3'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def step3(self, request):
        serializer = SignUpStep3Serializer(data=request.data)
        if serializer.is_valid():
            data = request.session.get('signup_data', {})
            cleaned_data = serializer.validated_data
            for key in ['height', 'weight']:
                if key in cleaned_data:
                    cleaned_data[key] = str(cleaned_data[key])
            data.update(cleaned_data)
            request.session['signup_data'] = data
            return Response({'message': 'Proceed to step 4'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def step4(self, request):
        serializer = SignUpStep4Serializer(data=request.data)
        if serializer.is_valid():
            data = request.session.get('signup_data', {})
            data.update(serializer.validated_data)
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
                    return Response({'message': 'Signup complete, user logged in'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        form = LoginForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return Response({'message': 'User logged in'}, status=status.HTTP_200_OK)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
    
class MyCalorieView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'mycalorie.html')
        else:
            return redirect('user_login')