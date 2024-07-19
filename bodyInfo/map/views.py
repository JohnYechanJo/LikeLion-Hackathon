from django.shortcuts import render
from .models import Restaurant
# Create your views here.

def mapview(request):
    restaurants = Restaurant.objects.all
    return render(request, "default.html", {'restaurants':restaurants})
