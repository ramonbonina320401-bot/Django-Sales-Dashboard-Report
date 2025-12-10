from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not email or not password:
            messages.error(request, 'Please provide both email and password.')
            return render(request, 'accounts/login.html')
        
        # Try to find user by email (username is stored as email)
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'accounts/login.html')
        
        # Authenticate with username and password
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('sales')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if not all([fullname, email, password, confirm_password]):
            messages.error(request, 'All fields are required.')
            return render(request, 'accounts/signup.html')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/signup.html')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'accounts/signup.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'accounts/signup.html')
        
        # Check if username (email) already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, 'An account with this email already exists.')
            return render(request, 'accounts/signup.html')
        
        # Split full name into first and last name
        name_parts = fullname.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        try:
            # Create user (username is email)
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Auto login after signup
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {first_name}!')
            return redirect('sales')
            
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'accounts/signup.html')
    
    return render(request, 'accounts/signup.html')

def logout_view(request):
    """Logout user and redirect to login page"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')