from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as django_login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('photo:list')
        else:
            print("invalid")
            return render(request, 'accounts/login.html', {'form': LoginForm})
    else:
        return render(request, 'accounts/login.html', {'form': LoginForm})


def agreement(request):
    return render(request, 'accounts/agreement.html')


def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            django_login(request, user)
            return render(request, 'accounts/agreement.html')
        else:
            print(signup_form.errors)
            print(signup_form.non_field_errors)
            signup_form = CustomUserCreationForm()
            # messages.error(request, signup_form.non_field_errors())
            return render(request, 'accounts/signup.html', {'form': signup_form, 'signUpFailed': True})
    else:
        signup_form = CustomUserCreationForm()
        return render(request, 'accounts/signup.html', {'form': signup_form, 'signUpFailed': False})
