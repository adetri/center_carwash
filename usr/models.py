

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
import random
from outlet.models import *

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')

        # Normalize the username (e.g., convert to lowercase)
        username = self.normalize_email(username)

        user = self.model(username=username, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        
        user.set_password(password)
        user.save(using=self._db)
      
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)


        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    # You can adjust the max_length as needed
    username = models.CharField(unique=True, max_length=255)
    is_block = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # Use the 'username' field for authentication

    def __str__(self):
        return self.username

    def normalize_username(self, username):
        return username.lower()
    
    @staticmethod
    def generate_random_otp():
        return random.randint(1000, 9999)
    


class UserOutlet(models.Model):
    usr = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    outlet = models.ForeignKey(Outlet, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.usr

