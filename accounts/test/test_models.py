from django.test import TestCase
from accounts.models import Users
from model_bakery import baker


class TestUserModel(TestCase):
    def setUp(self):
        self.user = baker.make(Users, username='mrg')
    
    def test_mobile_phone(self):
        self.assertEqual(str(self.user), 'mrg')