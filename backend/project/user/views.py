from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from finance.models import FinancialData
import csv
from datetime import datetime
from django.contrib import messages
from finance.forecast import generate_forecasts

@never_cache
def register(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the user first
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Handle the financial data file
            financial_data_file = request.FILES.get('financial_data_file')
            if financial_data_file:
                # Validate file extension
                if not financial_data_file.name.endswith('.csv'):
                    messages.error(request, "Invalid file format. Please upload a CSV file.")
                    return render(request, 'login.html', {'form': form})

                # Validate CSV file structure
                try:
                    decoded_file = financial_data_file.read().decode('utf-8').splitlines()
                    reader = csv.DictReader(decoded_file)

                    # Check for required columns
                    required_columns = [
                        'Date', 'Segment', 'Country', 'Product', 'Units Sold',
                        'Manufacturing Price', 'Sale Price', 'Gross Sales',
                        'Discounts', 'Sales', 'COGS', 'Profit'
                    ]
                    if not all(column in reader.fieldnames for column in required_columns):
                        messages.error(request, "Invalid CSV format. Missing required columns.")
                        print("Invalid csv format")
                        return render(request, 'login.html', {'form': form})

                    # Create FinancialData records for the user
                    for row in reader:
                        FinancialData.objects.create(
                            user=user,
                            date=datetime.strptime(row['Date'], '%Y-%m-%d').date(),
                            segment=row['Segment'],
                            country=row['Country'],
                            product=row['Product'],
                            units_sold=int(row['Units Sold']),
                            manufacturing_price=float(row['Manufacturing Price']),
                            sale_price=float(row['Sale Price']),
                            gross_sales=float(row['Gross Sales']),
                            discounts=float(row['Discounts']),
                            sales=float(row['Sales']),
                            cogs=float(row['COGS']),
                            profit=float(row['Profit'])
                        )

                    messages.success(request, "File uploaded and processed successfully!")
                except Exception as e:
                    messages.error(request, f"Error processing CSV file: {str(e)}")
                    print("Invalid csv format")
                    return render(request, 'login.html', {'form': form})

            # Log the user in and redirect to the dashboard
            user.backend = 'user.backends.UserProfileBackend'
            login(request, user)
            generate_forecasts(user.email)
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = UserProfileForm()
        print("Rendering login.html with form")  # Debug statement

    return render(request, 'login.html', {'form': form})

@never_cache
def user_login(request):
    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            generate_forecasts(user.email)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def home(request):
    return render(request, 'home.html')