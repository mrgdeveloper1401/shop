from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from accounts.managers import UsersManager
from django.utils import timezone

from core.models import UpdateMixin, CreateMixin


class User(AbstractBaseUser, CreateMixin, UpdateMixin, PermissionsMixin):
    mobile_phone = models.CharField(_('Mobile Phone'), max_length=15, unique=True)
    is_verify = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = 'mobile_phone'

    objects = UsersManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'


class State(CreateMixin, UpdateMixin):
    state = models.CharField(_("state"), max_length=30)
    i_active = models.BooleanField(default=True)

    def __str__(self):
        return self.state

    class Meta:
        db_table = 'state'
        verbose_name = _('state')
        verbose_name_plural = _('states')


class City(CreateMixin, UpdateMixin):
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='city')
    city = models.CharField(_("city"), max_length=30)
    i_active = models.BooleanField(default=True)

    def __str__(self):
        return self.city

    class Meta:
        db_table = 'city'
        verbose_name = _('city')
        verbose_name_plural = _('cities')


class Profile(CreateMixin, UpdateMixin):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    first_name = models.CharField(_("first name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True, null=True)
    email = models.EmailField(_('email'), blank=True, null=True)
    nation_code = models.CharField(_("nation code"), max_length=10, blank=True, null=True)

    class GenderChoices(models.TextChoices):
        male = 'male'
        female = 'female'
    gender = models.CharField(_("gender"), max_length=6, choices=GenderChoices.choices, default=GenderChoices.male)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='city_profile')
    sheba_number = models.CharField(_("sheba number"), max_length=24, blank=True, null=True)

    @property
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return f'{self.user.mobile_phone} {self.get_full_name}'

    class Meta:
        db_table = 'profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


class Otp(CreateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_otp')
    code = models.PositiveIntegerField(_("code"), blank=True)
    expired_at = models.DateTimeField(_("expired at"), blank=True, null=True)

    @property
    def generate_code(self):
        from random import choices
        from string import digits
        code = choices(digits, k=8)
        return code

    def save(self, *args, **kwargs):
        self.code = self.generate_code
        self.expired_at = timezone.now() + timezone.timedelta(minutes=2)
        return super().save(*args, **kwargs)
