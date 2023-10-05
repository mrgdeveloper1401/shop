from django.test import SimpleTestCase
from accounts.views import UserRegisterVerifyCodeView, UserRegisterView, LoginView
from django.urls import reverse, resolve


# class TestUrls(SimpleTestCase):
#     def test_verify_code(self):
#         url_verify = reverse('accounts:verify_account')
#         self.assertEqual(resolve(url_verify).func.view_class, UserRegisterVerifyCodeView)
        
#     def test_signup(self):
#         url_signup = reverse('accounts:signup')
#         self.assertEqual(resolve(url_signup).func.view_class, UserRegisterView)
        
#     def test_login(self):
#         url_login = reverse('accounts:login')
#         self.assertEqual(resolve(url_login).func.view_class, LoginView)




