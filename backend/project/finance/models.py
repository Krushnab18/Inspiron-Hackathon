from django.db import models
from user.models import UserProfile
# Create your models here.

from django.db import models

class FinancialData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)  # Link to the user
    date = models.DateField()
    segment = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    units_sold = models.IntegerField()
    manufacturing_price = models.FloatField()
    sale_price = models.FloatField()
    gross_sales = models.FloatField()
    discounts = models.FloatField()
    sales = models.FloatField()
    cogs = models.FloatField()
    profit = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.product}"
