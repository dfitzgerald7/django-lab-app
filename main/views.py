from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def homepage(request):
    return render(request, 
                  'main/homepage.html',
                  context={'labs': request.user.lab_set.all()})

def signup(request):
    if request.method == "POST":  
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, 
                  'main/signup.html',
                  context={'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('main:homepage')
            else:
                messages.error(request, 'Invalid username or password')
        else: 
            messages.error(request, 'Invalid username or password. Likely missing a field.')
   
    form = AuthenticationForm
    return render(request, 
                  'main/login.html',
                  {'form': form})


def logout_request(request):
    logout(reqeust)
    messages.info(request, 'Logged out successfully')
    return redirect('main:homepage')

def new_lab(request):
    