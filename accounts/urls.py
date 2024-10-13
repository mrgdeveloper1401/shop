from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from accounts.views import CreateOtpApiView, VerifyOtpApiView

# router = DefaultRouter()
# router.register('create_otp_code', CreateOtpViewSet, basename='otp')

app_name = 'accounts'
urlpatterns = [
    # path('', include(router.urls)),
    path('create_otp_code/', CreateOtpApiView.as_view(), name='create_otp_code'),
    path('verify_otp/', VerifyOtpApiView.as_view(), name='verify_otp'),
]
