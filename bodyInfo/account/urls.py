from django.urls import path
from .views import LoginView, LogoutView, SignUpStep1View, SignUpStep2View, SignUpStep3View, SignUpStep4View, MyCalorieView

urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('signup/step1/', SignUpStep1View.as_view(), name='signup_step1'),
    path('signup/step2/', SignUpStep2View.as_view(), name='signup_step2'),
    path('signup/step3/', SignUpStep3View.as_view(), name='signup_step3'),
    path('signup/step4/', SignUpStep4View.as_view(), name='signup_step4'),
    path('mycalorie/', MyCalorieView.as_view(), name='mycalorie'),
]