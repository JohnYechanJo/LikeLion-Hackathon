from django.urls import path
from .views import LoginView, LogoutView, SignUpViewSet, MyCalorieView

urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('signup/step1/', SignUpViewSet.as_view({'post': 'step1'}), name='signup_step1'),
    path('signup/step2/', SignUpViewSet.as_view({'post': 'step2'}), name='signup_step2'),
    path('signup/step3/', SignUpViewSet.as_view({'post': 'step3'}), name='signup_step3'),
    path('signup/step4/', SignUpViewSet.as_view({'post': 'step4'}), name='signup_step4'),
    path('mycalorie/', MyCalorieView.as_view(), name='mycalorie'),
]