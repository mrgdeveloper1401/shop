from rest_framework.serializers import Serializer, ModelSerializer, CharField, IntegerField
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.models import User, Otp


class OtpSerializer(Serializer):
    mobile_phone = CharField()

    def validate_mobile_phone(self, data):
        user = User.objects.filter(mobile_phone=data)
        if not user:
            raise ValidationError({'mobile_phone': _("شماره موبایل وجود ندارد لطفا ابتدا حساب خود را بسازید")})
        return data

    def validate(self, attr):
        otp = Otp.objects.filter(user__mobile_phone=attr['mobile_phone']).last()
        if otp:
            if otp.check_expired_otp:
                otp.delete_otp_code()
            else:
                raise ValidationError({"otp": 'شمار از قبل یه کد دارید لطفا به مدت 2 دقیقه صبر کنید'})
        return attr

    def create(self, validated_data):
        user = User.objects.get(mobile_phone=validated_data['mobile_phone'])
        return Otp.objects.create(user=user)


class VerifyOtpSerializer(Serializer):
    code = IntegerField()

    def validate_code(self, data):
        otp = Otp.objects.filter(code=data).last()
        try:
            Otp.objects.get(code=data)
        except Otp.DoesNotExist:
            raise ValidationError({"code": "کد شما نادرست هست"})
        if otp.check_expired_otp:
            otp.delete_otp_code()
            raise ValidationError({"code": "کد شما منقضی شده هست لطفا دوباره درخواست خود کنید"})
        return data

    def validate(self, attrs):
        otp = Otp.objects.get(code=attrs['code'])
        user = User.objects.get(mobile_phone=otp.user.mobile_phone)
        if not user.is_verify:
            user.is_verify = True
            user.is_active = True
            user.save()
            otp.delete()
        else:
            otp.delete()
            raise ValidationError({'code': "حساب شما از قبل تایید شده هست"})
        return attrs
    
    def create(self, validated_data):
        return super().create(validated_data)
