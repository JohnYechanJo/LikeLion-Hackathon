from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class SignUpFormStep1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("중복된 아이디입니다.")
        return username
    

class SignUpFormStep2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'age', 'email', 'phone_number']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("이미 가입된 이메일입니다.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("이미 가입된 전화번호입니다.")
        return phone_number
    
class SignUpFormStep3(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', '남자'),
        ('F', '여자'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    height = forms.DecimalField(max_digits=5, decimal_places=2)
    weight = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Profile
        fields = ['gender', 'height', 'weight']

class SignUpFormStep4(forms.ModelForm):
    exercise_frequency = forms.IntegerField(help_text="운동을 주 몇 회 하는지 입력하세요")

    class Meta:
        model = Profile
        fields = ['exercise_frequency']