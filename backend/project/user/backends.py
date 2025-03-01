# accounts/backends.py
from django.contrib.auth.backends import BaseBackend
from .models import UserProfile
from django.contrib.auth.hashers import check_password

class UserProfileBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(email=email)
            if check_password(password, user.password):  # Verify the password
                return user
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None