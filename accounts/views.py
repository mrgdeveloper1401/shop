from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
import random
from .form import UserRegisterForm
from shop.utils import send_otp_code
from .models import Otpcode
from .form import VerifyAccountsForm, UserLoginForm
from .models import Users



class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(10000, 99999)
            send_otp_code(cd['email'], random_code)
            Otpcode.objects.create(email=cd['email'], code=random_code)
            request.session['user_register_info'] = {
                'username': cd['username'],
                'email': cd['email'],
                'first_name': cd['first_name'],
                'last_name': cd['last_name'],
                'password': cd['password']
                
            }
            messages.success(request, 'successfully registered account and we send code for verify account', 'success')
            return redirect('accounts:verify_account')
        return render(request, self.template_name, {'form': form})
    

class UserRegisterVerifyCodeView(View):
    form_class = VerifyAccountsForm
    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/verify_account.html', {'form': form})
    
    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = Otpcode.objects.get(email=user_session['email'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                user = Users.objects.create_user(
                    username=user_session['username'],
                    email=user_session['email'],
                    first_name=user_session['first_name'],
                    last_name=user_session['last_name'],
                    password=user_session['password']
                )
                code_instance.delete()
                user.save()
                messages.success(request,'successfully registered account and we send code for verify account','success')
                return redirect('accounts:login')
            else:
                messages.error(request, 'wrong code', 'error')
                return redirect('accounts:account_verify')
            
            
class LoginView(View):
    form_class = UserLoginForm
    temlated_name = 'accounts/login.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.temlated_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'successfully login','success')

            else:
                messages.error(request, 'wrong username or password', 'error')
                return redirect('accounts:login')
        return render(request, self.temlated_name, {'form': form})
    

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated == request.user.id:
            logout(request)
        messages.error(request, 'invalid', 'warning')


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'
    
    
class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
    
    
class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')
    

class UserPasswordResetComplateView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'