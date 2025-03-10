# accounts/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    company_size = models.CharField(max_length=50)
    annual_revenue = models.DecimalField(max_digits=15, decimal_places=2, null=True,  blank=True)
    role = models.CharField(max_length=50)

    # Required fields for Django's authentication system
    is_staff = models.BooleanField(default=False)  # Controls admin access
    is_active = models.BooleanField(default=True)  # Required for all users
    date_joined = models.DateTimeField(default=timezone.now)  # Optional but recommended

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['name']  # Fields required when creating a user

    objects = UserProfileManager()  # Assign the custom manager

    def __str__(self):
        return self.email

    # Required method for admin access
    def has_module_perms(self, app_label):
        return self.is_staff  # Only staff users have admin access