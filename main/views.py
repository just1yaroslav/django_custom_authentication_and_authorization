from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from users.models import CustomUser
from main.forms import RegisterUserForm, LoginUserForm


def index(request):
    return render(request, 'main/index.html')


def register_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('main:login')
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})


def login_user(request):
    form = LoginUserForm()
    if request.method == 'POST':
        form = LoginUserForm(None, request.POST or None)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main:index')
    else:
        form = LoginUserForm()

    return render(request, 'main/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('main:index')
