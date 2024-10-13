from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from accounts.models import User, Otp
from accounts.serializers import OtpSerializer, VerifyOtpSerializer


class CreateOtpApiView(APIView):
    @extend_schema(
        description='send otp code',
        request=OtpSerializer,
        responses={201: HTTP_201_CREATED}
    )
    def post(self, request):
        ser_data = OtpSerializer(data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response({"کد شما با موفقیت ارسال شد"}, status=HTTP_201_CREATED)


class VerifyOtpApiView(APIView):
    @extend_schema(
        description='verify user with otp code',
        request=VerifyOtpSerializer,
        responses={201: HTTP_200_OK}
    )
    def post(self, request):
        ser_data = VerifyOtpSerializer(data=request.data)
        ser_data.is_valid(raise_exception=True)
        return Response({"شما با موفقیت احراز هویت شدید"}, status=HTTP_200_OK)
