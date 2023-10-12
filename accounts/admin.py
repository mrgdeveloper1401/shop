from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from .form import UsersCreationForms, UsersChangeForms
from .models import UsersModel, Otpcode, UserMoreInformationModel, UserWalletModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(UsersModel)
class UsersAdmin(BaseUserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "username")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    form = UsersChangeForms
    add_form = UsersCreationForms
    change_password_form = AdminPasswordChangeForm
    list_display = ("username", "email", 'mobile_phone', "first_name", "last_name", "is_staff", 'is_active', 'is_superuser')
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("mobile_phone", "first_name", "last_name", "email")
    readonly_fields = ('date_joined',)
    # ordering = ("emai",)
    filter_horizontal = ()
    list_display_links = ('username', 'email', 'mobile_phone')
    
    
@admin.register(UserMoreInformationModel)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = ('province', 'thonship', 'city', 'postal_code')
    list_filter = ("province", "thonship", "city", 'create_at')


@admin.register(UserWalletModel)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_filter = ('user', 'create_at')


@admin.register(Otpcode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'created_at')