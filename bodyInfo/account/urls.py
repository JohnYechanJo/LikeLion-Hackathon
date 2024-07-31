from django.urls import path
from .views import user_login, user_logout, signup_step1, signup_step2, signup_step3, signup_step4, mycalorie

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/step1/', signup_step1, name='signup_step1'),
    path('signup/step2/', signup_step2, name='signup_step2'),
    path('signup/step3/', signup_step3, name='signup_step3'),
    path('signup/step4/', signup_step4, name='signup_step4'),
    path('mycalorie/', mycalorie, name='mycalorie'),
]
