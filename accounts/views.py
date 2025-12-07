from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')

from django.shortcuts import render, redirect

def login_view(request):
    # Check if the "Login" button was clicked
    if request.method == 'POST':
        # --- DEVELOPMENT MODE: BYPASS VALIDATION ---
        # We don't check the database or password.
        # We just redirect immediately to the 'sales' dashboard.
        return redirect('sales')

    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')