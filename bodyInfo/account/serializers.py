# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Profile
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("중복된 아이디입니다.")
        return value

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname', 'age', 'email', 'phone_number', 'gender', 'height', 'weight', 'exercise_frequency']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이미 가입된 이메일입니다.")
        return value

    def validate_phone_number(self, value):
        if Profile.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("이미 가입된 전화번호입니다.")
        return value

class SignUpStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("중복된 아이디입니다.")
        return value

class SignUpStep2Serializer(serializers.ModelSerializer):
    phone_regex = RegexValidator(regex=r'^\d{10,15}$', message="전화번호는 10~15자리 숫자여야 합니다.")
    phone_number = serializers.CharField(validators=[phone_regex], max_length=15)

    class Meta:
        model = Profile
        fields = ['nickname', 'age', 'email', 'phone_number']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이미 가입된 이메일입니다.")
        return value

    def validate_phone_number(self, value):
        if Profile.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("이미 가입된 전화번호입니다.")
        return value

class SignUpStep3Serializer(serializers.ModelSerializer):
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]

    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    height = serializers.DecimalField(max_digits=5, decimal_places=2)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Profile
        fields = ['gender', 'height', 'weight']

class SignUpStep4Serializer(serializers.ModelSerializer):
    exercise_frequency = serializers.IntegerField(help_text="운동을 주 몇 회 하는지 입력하세요")

    class Meta:
        model = Profile
        fields = ['exercise_frequency']
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")

        data['user'] = user
        return data