from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Choices for industry
INDUSTRY_CHOICES = [
    ('retail', 'Retail'),
    ('ecommerce', 'E-Commerce'),
    ('manufacturing', 'Manufacturing'),
    ('other', 'Other'),
]

# Choices for company size
COMPANY_SIZE_CHOICES = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
]

# Choices for role
ROLE_CHOICES = [
    ('ceo', 'CEO'),
    ('finance_manager', 'Finance Manager'),
    ('other', 'Other'),
]

class UserProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    password = models.CharField(max_length=128, verbose_name="Password")  # Store hashed passwords
    password_confirmation = models.CharField(max_length=128, verbose_name="Confirm Password")  # For validation only
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, verbose_name="Industry")
    company_size = models.CharField(max_length=50, choices=COMPANY_SIZE_CHOICES, verbose_name="Company Size")
    annual_revenue = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        validators=[MinValueValidator(0)], 
        verbose_name="Annual Revenue"
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, verbose_name="Role")

     # Required fields for Django's authentication system
    last_login = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['name']  # Fields required when creating a user

    def __str__(self):
        return self.email  # Display email as the identifier in the admin panel

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"