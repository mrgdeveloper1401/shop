from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from accounts.managers import UsersManager

class Users(AbstractUser):
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, unique=True, blank=True, null=True)
    gender = (
        ('male', 'male'),
        ('female', 'female'),
    )
    email = models.EmailField(_("email address"), blank=True, unique=True)
    gender_choose = models.CharField(_('gender'), max_length=6, blank=True, choices=gender, default='male')
    objects = UsersManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name') 
    
    def __str__(self):
        return self.username
    
    @property
    def is_admin(self):
        return self.is_staff
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
        

class Otpcode(models.Model):
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    code = models.PositiveIntegerField()
    created_at = models.DateTimeField(_('create code'), auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.email} -- {self.code}'