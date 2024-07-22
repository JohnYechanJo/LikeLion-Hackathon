from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    AGE_GROUP_CHOICES = [
        ('Adult', 'Adult'),
        ('Teen', 'Teen'),
    ]

    height = models.FloatField()  # cm
    weight = models.FloatField()  # kg
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=10, choices=AGE_GROUP_CHOICES)
    exercise_frequency = models.IntegerField()  # times per week

    def __str__(self):
        return f"{self.gender} {self.age_group} - {self.height} cm, {self.weight} kg, {self.exercise_frequency} times/week"
    
