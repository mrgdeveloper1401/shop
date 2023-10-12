from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from accounts.managers import UsersManager
from django.utils import timezone


class UsersModel(AbstractBaseUser):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    username = models.CharField(_('Username'), max_length=100, unique=True)
    email = models.EmailField(_('Email'), max_length=255, unique=True)
    mobile_phone = models.CharField(_('Mobile Phone'), max_length=15, unique=True)
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(_('Gender'), max_length=6, choices=gender, default='Male')
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Superuser'), default=False)
    date_joined = models.DateTimeField(_('create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('update at'), auto_now=True)
    last_login = models.DateTimeField(_('last login'), default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'mobile_phone']
    objects = UsersManager()
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class UserWalletModel(models.Model):
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE)
    balance = models.DecimalField(_('Balance'), max_digits=10, decimal_places=3)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('update at'), auto_now=True)


    class Meta:
        verbose_name = 'user wallet'
        verbose_name_plural = 'user wallets'
        db_table = 'user_wallet'
        

class UserMoreInformationModel(models.Model):
    user = models.OneToOneField(UsersModel, on_delete=models.CASCADE)
    province = models.CharField(_('Province'), max_length=100,
                                help_text='enter province name')
    thonship = models.CharField(_('Thonship'), max_length=100,
                                help_text='enter thonship name')
    city = models.CharField(_('City'), max_length=100,
                                help_text='enter city name')
    address = models.CharField(_('Address'), max_length=100,
                                help_text='enter address')
    postal_code = models.CharField(_('Postal Code'), max_length=10)
    birth_day = models.DateField(_('Birthday'), null=True, blank=True, default=timezone.now)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True)
    update_at = models.DateTimeField(_('update at'), auto_now=True)
    
    
    class Meta:
        verbose_name = 'user more information'
        verbose_name_plural = 'user more information'
        db_table = 'user_more_information'
    
    
class Otpcode(models.Model):
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    code = models.PositiveIntegerField()
    created_at = models.DateTimeField(_('create code'), auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.email} -- {self.code}'