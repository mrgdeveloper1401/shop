from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='signup'),
    path('register/verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_account'),
    path('login/', views.LoginView.as_view(), name='login'),
    
]
