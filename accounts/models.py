from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, unique=True, blank=True)
    gender = (
        'male', 'male',
        'female', 'female'
    )
    gender_choose = models.CharField(_('gender'), max_length=6, blank=True, choices=gender, default='male')
    