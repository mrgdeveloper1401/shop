from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager

class User(AbstractUser):
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, unique=True, blank=True)
    gender = (
        'male', 'male',
        'female', 'female'
    )
    gender_choose = models.CharField(_('gender'), max_length=6, blank=True, choices=gender, default='male')
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'mobile_phone', 'first_name', 'last_name') 
    
    @property
    def is_admin(self):
        return self.is_staff
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'