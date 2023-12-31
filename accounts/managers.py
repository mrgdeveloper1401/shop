from django.contrib.auth.models import BaseUserManager, UserManager


class UsersManager(UserManager):
    def create_user(self, username, email, first_name, last_name, mobile_phone, password=None):
        if not username:
            raise ValueError('please enter username')
        if not first_name:
            raise ValueError('please enter first name')
        if not last_name:
            raise ValueError('please enter last name')
        if not email:
            raise ValueError('please enter email')
        if not mobile_phone:
            raise ValueError('please enter mobile phone')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile_phone=mobile_phone,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, first_name, last_name, mobile_phone, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            mobile_phone=mobile_phone
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user