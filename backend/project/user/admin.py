# accounts/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('email', 'name', 'company_name', 'industry', 'company_size', 'annual_revenue', 'role')

    # Filters for the list view
    list_filter = ('industry', 'company_size', 'role')

    # Search functionality
    search_fields = ('email', 'name', 'company_name')

    # Group fields into sections in the edit form
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'password'),
        }),
        ('Company Information', {
            'fields': ('company_name', 'industry', 'company_size', 'annual_revenue'),
        }),
        ('Role', {
            'fields': ('role',),
        }),
    )

    # Make the password field read-only in the admin panel
    readonly_fields = ('password',)