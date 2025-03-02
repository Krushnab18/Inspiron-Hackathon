from django.contrib import admin
from .models import FinancialData

@admin.register(FinancialData)
class FinancialDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'product', 'profit')  # Fields to display in the list view
    list_filter = ('user', 'date', 'product')  # Add filters for these fields
    search_fields = ('product', 'segment', 'country')  # Add search functionality

    # Restrict access to only the logged-in user's data (if not a superuser)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers can see all data
        return qs.filter(user=request.user)  # Regular users can only see their data

    # Automatically set the user when adding a new FinancialData record
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user  # Set the user to the currently logged-in user
        super().save_model(request, obj, form, change)