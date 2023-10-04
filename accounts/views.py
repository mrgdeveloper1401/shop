from django.shortcuts import render
from django.views import View
from .form import UserRegisterForm



class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
        
    def post(self, request):
        ...
