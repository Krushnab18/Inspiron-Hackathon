from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    financial_data_file = forms.FileField(required=False)  # Add a file upload field

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'password_confirmation', 'company_name', 'industry', 'company_size', 'annual_revenue', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Passwords do not match.")