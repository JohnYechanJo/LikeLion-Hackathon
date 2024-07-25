"""
URL configuration for bodyInfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from map import views as m
from bodyCalculate import views as cal

urlpatterns = [
    path("admin/", admin.site.urls),
    path('bodyCalculate/', cal.calculate_metrics, name="calculate_metrics"),
    path('mapview/', m.mapview, name="mapview"),
    path('mapview/list/', m.re_list, name="re_list"),
    path('mapview/salad', m.map_salad, name="map_salad"),
    path('test/', m.test, name="test"),
]
