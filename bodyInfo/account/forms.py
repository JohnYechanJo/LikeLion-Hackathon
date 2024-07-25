from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    age = forms.IntegerField(required=True)
    height = forms.DecimalField(max_digits=5, decimal_places=2)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)
    exercise_frequency = forms.IntegerField(help_text="운동을 주 몇 회 하는지 입력하세요")

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'phone_number', 'gender', 'age', 'height', 'weight', 'exercise_frequency']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.set_password(self.cleaned_data['password'])  # 패스워드 암호화
            user.save()
        return user
    
    def clean_id(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("중복된 아이디입니다.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("이미 가입된 이메일입니다.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(profile__phone_number=phone_number).exists():
            raise ValidationError("이미 가입된 전화번호입니다.")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
