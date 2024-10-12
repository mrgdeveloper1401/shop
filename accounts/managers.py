from django.contrib.auth.models import BaseUserManager


class UsersManager(BaseUserManager):
    def create_user(self, mobile_phone, password=None):
        if not mobile_phone:
            raise ValueError('please enter mobile phone')
        user = self.model(mobile_phone=mobile_phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_phone, password=None):
        user = self.create_user(password=password, mobile_phone=mobile_phone)
        user.is_staff = True
        user.is_superuser = True
        user.is_verify = True
        user.save(using=self._db)
        return user
