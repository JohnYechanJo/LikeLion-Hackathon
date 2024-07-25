from django.urls import path
from .views import user_login, logout, signup

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
]
