from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'gender', 'age_group', 'exercise_frequency']
        widgets = {
            'gender': forms.RadioSelect,
            'age_group': forms.RadioSelect,
        }