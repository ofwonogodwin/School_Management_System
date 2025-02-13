from django.shortcuts import render, redirect
from .models import Destination
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def add(request):
    if request.method == 'POST':
        name = request.POST.get('schoolName')
        level = request.POST.get('schoolLevel')
        location = request.POST.get('schoolLocation')
        num_students = request.POST.get('numStudents')

        Destination.objects.create(name=name, level=level, location=location, num_students=num_students)

        return redirect('success')  # Redirect to a success page

    return render(request, 'home.html')

#user registration view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')

# Dashboard View (After Login)
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    return redirect('login')
def success(request):
    return render(request,'success.html')

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')
