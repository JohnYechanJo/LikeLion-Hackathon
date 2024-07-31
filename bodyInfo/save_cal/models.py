from django.db import models
from account.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class FoodCal(models.Model):
    hamberger = models.IntegerField(default=0, null=False)
    pizza = models.IntegerField(default=0, null=False)
    chicken = models.IntegerField(default=0, null=False)

class ExerciseCal(models.Model): #30분 단위로 저장.
    walk = models.IntegerField(default=0, null=False)
    run = models.IntegerField(default=0, null=False)
    weight_training = models.IntegerField(default=0, null=False)

class UserCal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()  # 날짜 정보 추가
    hamberger = models.IntegerField(default=0, null=False)
    pizza = models.IntegerField(default=0, null=False)
    chicken = models.IntegerField(default=0, null=False)
    walk = models.IntegerField(default=0, null=False)
    run = models.IntegerField(default=0, null=False)
    weight_training = models.IntegerField(default=0, null=False)

    def __str__(self):
        return f"{self.user.username}의 기록 - {self.date}"
