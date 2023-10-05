from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Users
from accounts.form import UserRegisterForm


class TestUserRegisterView(TestCase):
    # for send request
    def setUp(self):
        self.client = Client()
        
    def test_user_register_GET(self):
        responce = self.client.get(reverse('accounts:signup'))
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'accounts/register.html')
        self.failUnless(responce.context['form'], UserRegisterForm)
        
    def test_user_register_POST_valid(self):
        responce = self.client.post(reverse('accounts:signup'), 
        data={
            'username':'mrgdeveloper',
            'email':'m.goodarzi606@gmail.com',
            'first_name':'mohammad',
            'last_name': 'goodarzi',
            'password': '<PASSWORD>'
        }
        )
        self.assertEqual(responce.status_code, 302)
        self.assertRedirects(responce, reverse('accounts:verify_account'))
        self.assertEqual(Users.objects.count(), 0)
        
    def test_user_register_POST_invalid(self):
        responce = self.client.post(reverse('accounts:signup'), 
        data={
            'username':'mrgdeveloper',
            'email':'m.goodarzi606gmail.com',
            'first_name':'mohammad',
            'last_name': 'goodarzi',
            'password': '<PASSWORD>'
        }
        )
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'accounts/register.html')
        self.failIf(responce.context['form'].is_valid())
        self.assertFormError(form=responce.context['form'], field='email', errors=['Enter a valid email address.'])
        
        
        def test_user_login(self):
            pass