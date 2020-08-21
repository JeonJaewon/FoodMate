from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login as django_login
from .forms import CustomUserCreationForm, LoginForm, basic_info_form
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import PasswordChangeForm

def login(request):
    login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if login_form.is_valid():
            # username = request.POST['username']
            # password = request.POST['password']
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # 해당 유저가 존재한다면 바로 로그인
            if user is not None:
                django_login(request, user)
                return redirect('photo:list')
            login_form.add_error(None, "login_failed")
    return render(request, 'accounts/login.html', {'form': login_form})


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

@login_required
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

from django.contrib.auth import update_session_auth_hash

def login_update(request):
    if request.method == 'POST':
        user_change_form = PasswordChangeForm(request.user, request.POST)
        user_email = request.user
        user_email.email = request.POST["email"]
        user_email.save()
        if user_change_form.is_valid():
            user = user_change_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:login')

    else:
        user_change_form = PasswordChangeForm(request.user)
    return render(request, 'accounts/login_info.html', {
        'user_change_form': user_change_form,
    })

def security(request):
    current_user = request.user
    return render(request, 'accounts/security.html', {'user': current_user})

from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

def delete(request):
    request.user.delete()
    logout(request)
    return redirect('accounts:login')

