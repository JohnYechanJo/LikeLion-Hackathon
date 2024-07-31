from django.urls import path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    #path('', calculate_metrics, name='calculate_metrics'),
    path('profile/', profile_view, name='profile'),
    path('calorie_input/', calorie_input_view, name='calorie_input'),
    path('calorie_output/', calorie_output_view, name='calorie_output'),
]