from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from accounts.models import User, City, State, Otp, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("mobile_phone", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verify",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("mobile_phone", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("mobile_phone", "is_active", "is_staff", "is_superuser", "is_verify")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "is_verify")
    search_fields = ("mobile_phone",)
    ordering = ("mobile_phone",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ['created_at', "updated_at", "last_login"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', "last_name", "user", "birth_date", "city"]
    search_fields = ['first_name', "last_name", "user__mobile_phone", "city"]
    list_display_links = ['first_name', 'last_name', "user"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['user', "code", "created_at", "expired_at"]
