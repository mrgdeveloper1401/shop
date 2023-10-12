from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('register/', views.UserRegisterView.as_view(), name='signup'),
    # path('register/verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_account'),
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('reset/', views.UserPasswordResetView.as_view(), name='password_reset_form'),
    # path('reset/done/', views.UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/complete/', views.UserPasswordResetComplateView.as_view(), name='password_reset_complete'),
]
