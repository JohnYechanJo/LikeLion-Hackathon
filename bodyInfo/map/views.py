from django.shortcuts import render
# Create your views here.

def mapview(request):
    return render(request, "result.html")