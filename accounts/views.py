from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('sales')
    
    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        
        # Validation
        if not fullname or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'accounts/signup.html')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/signup.html')
        
        if len(password) < 6:
            messages.error(request, 'Password must be at least 6 characters long.')
            return render(request, 'accounts/signup.html')
        
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'accounts/signup.html')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'accounts/signup.html')
        
        # Split full name into first and last name
        name_parts = fullname.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        
        # Create user
        try:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            # Auto login after registration
            login(request, user)
            messages.success(request, f'Welcome {first_name}! Your account has been created.')
            return redirect('sales')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'accounts/signup.html')
    
    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('sales')
    
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        if not email or not password:
            messages.error(request, 'Email and password are required.')
            return render(request, 'accounts/login.html')
        
        # Authenticate user (username is email)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('sales')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout_view(request):
    # Get message storage to clear all pending messages
    storage = messages.get_messages(request)
    storage.used = True  # Mark all messages as used to clear them
    
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')