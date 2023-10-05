from django import forms
from django.contrib.auth import password_validation
from .models import Users
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField



class UsersCreationForms(forms.ModelForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model = Users
        fields = ("username", 'email', 'mobile_phone', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
class UsersChangeForms(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="../password">this form</a>.'
        ),
    )

    class Meta:
        model = Users
        fields = "__all__"
        
    
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        widgets = {
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'password': forms.PasswordInput()
        }
        error_messages = {
            'username': {
                'required': 'please enter username.'
            },
            'email': {
                'required': 'please enter email address.',
            },
            'first_name': {
                'required': 'please enter first name.',
            },
            'last_name': {
                'required': 'please enter last name.',
            },
            'password': {
               'required': 'please enter password.',
            },
            'password2': {
               'required': 'please enter password confirmation.',}
            
        }
        
        
class VerifyAccountsForm(forms.Form):
    code = forms.IntegerField()


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(),
                             error_messages={'required': 'please enter email address'}, max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(),
                               error_messages={'required': 'please enter password'} , max_length=255)