from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

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
        return redirect('login')
        return render(request, 'login.html')


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