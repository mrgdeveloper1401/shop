from django.test import TestCase
from accounts.form import UserRegisterForm, UserloginForm
from accounts.models import Users
from model_bakery import baker


class TestRegisterForm(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Users.objects.create_user(
            username = 'mrgdeveloper',
            email = 'm.goodarzi606@gmail.com',
            first_name = 'mohammad',
            last_name = 'goodarzi',
            password = 'QazWSX.1234'
        )
        
    def test_valid_data(self):
        form = UserRegisterForm(data={
            'username':'mrgdeveloper',
            'email':'m.goodarzi606@gmail.com',
            'first_name':'mohammad',
            'last_name': 'goodarzi',
            'password': 'QazWSX.1234'
        })
        self.assertTrue(form.is_valid)
        
    def test_empaty_data(self):
        form = UserRegisterForm(data={})
        self.assertTrue(form.has_error)
        
    def test_email_exist(self):
        form = UserRegisterForm(
            data={
            'username':'admin',
            'email':'m.goodarzi606@gmail.com',
            'first_name':'mohammad',
            'last_name': 'goodarzi',
            'password': 'QazWSX.1234'
            }
        )
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('email'))
        
    def test_username_exist(self):
        form = UserRegisterForm(
            data={
            'username':'mrgdeveloper',
            'email':'mg@gmail.com',
            'first_name':'mohammad',
            'last_name': 'goodarzi',
            'password': 'QazWSX.1234'
            }
        )
        self.assertEqual(len(form.errors), 1)
        self.assertTrue(form.has_error('username'))
        
        
        
