from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .form import UserRegisterForm
import random
from shop.utils import send_otp_code
from .models import Otpcode



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
    

class UserRegisterVerifyCode(View):
    def get(self, request):
        pass
    
    def post(self, request):
        pass