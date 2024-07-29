from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=[('M', '남자'), ('F', '여자')])
    age = models.IntegerField(default=0, null=False)
    height = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    exercise_frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    