from django.urls import path, include
from django.contrib import admin
from .views import calculate_metrics
from account.views import *


urlpatterns = [
    path('', calculate_metrics, name='calculate_metrics'),
]