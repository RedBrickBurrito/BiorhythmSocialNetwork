from multiprocessing.sharedctypes import Value
from pyexpat import model
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, birthday, password):
        if not email:
            raise ValueError('The email must be set')
        if not birthday:
            raise ValueError('Birthday date must be set')
        email = self.normalize_email(email)
        birthday = birthday
        user = self.model(email=email, birthday=birthday)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, birthday, password):
        user = self.create_user(
            email=self.normalize_email(email),
            birthday=birthday,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    birthday = models.DateField(null=True, blank=False)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    BIRTHDAY_FIELD = 'birthday'
    REQUIRED_FIELDS = ['birthday']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True