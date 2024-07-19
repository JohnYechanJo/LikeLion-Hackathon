from django.urls import path
from .views import calculate_metrics

urlpatterns = [
    path('', calculate_metrics, name='calculate_metrics'),
]