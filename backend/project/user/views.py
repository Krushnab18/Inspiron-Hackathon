from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        company_name = request.POST['company_name']
        industry = request.POST['industry']
        company_size = request.POST['company_size']
        annual_revenue = request.POST['annual_revenue']
        role = request.POST['role']

        # Create the UserProfile
        user = UserProfile.objects.create(
            email=email,
            name=name,
            password=make_password(password),
            company_name=company_name,
            industry=industry,
            company_size=company_size,
            annual_revenue=annual_revenue,
            role=role,
        )
        user.save()

        # Log the user in
        login(request, user)
        return redirect('login')  # Redirect to the dashboard after registration
    else :
        return render(request, 'register.html')


@never_cache
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')