from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as django_login
from .forms import CustomUserCreationForm, LoginForm, basic_info_form
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

from .models import User

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # 해당 유저가 존재한다면
        if user is not None:
            django_login(request, user)
            return redirect('photo:list')
    return render(request, 'accounts/login.html', {'form': LoginForm})


def agreement(request):
    return render(request, 'accounts/agreement.html')


def signup(request):
    # POST 방식의 요청이라면 form을 post로 초기화하고, 아니면 none으로 초기화
    signup_form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if signup_form.is_valid():
            user = signup_form.save()
            django_login(request, user)
            return redirect('photo:list')
    return render(request, 'accounts/signup.html', {'form': signup_form})

def profile(request):
    current_user = request.user

    return render(request, 'accounts/profile.html', {'user': current_user})

from django.contrib.auth.forms import UserChangeForm

def update(request):
    if request.method == 'POST':
        user_change_form = basic_info_form(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('photo:list')

    else:
        user_change_form = basic_info_form(instance=request.user)
    return render(request, 'accounts/basic_info.html', {
        'user_change_form': user_change_form
    })