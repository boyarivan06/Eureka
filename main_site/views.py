from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from string import ascii_uppercase, ascii_lowercase, digits
from django.contrib.auth.decorators import login_required
from main_site.forms import RegisterForm, LoginForm
from main_site.models import User


def password_is_valid(raw_password):
    return len(raw_password) >= 8 and (set(raw_password) & set(ascii_uppercase)) \
           and (set(raw_password) & set(ascii_lowercase)) and (set(raw_password) & set(digits))


def index_view(request):
    return render(request, 'index.html', {'user': request.user})


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form.data['password'] != form.data['password_repeat']:
                context['message'] = f'Пароли не совпадают'
            elif not password_is_valid(form.data['password']):
                context['message'] = f'Пароль ненадёжен'
            elif not form.data['email']:
                context['message'] = 'Введите электронную почту'
            else:
                user = User(username=form.data['username'].lower(),
                               first_name=form.data['first_name'],
                               last_name=form.data['last_name'],
                               email=form.data['email'].lower( )
                               )
                user.set_password(form.data['password'])
                user.save()
                login(request, user)
                return redirect('index')
    context['form'] = RegisterForm()
    return render(request, "reg.html", context)


def login_view(request):
    context = {}
    if request.method == 'POST':
        print('catch post')
        form = LoginForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user = User.objects.filter(username=form.data['username']).first()
            if not user:
                user = User.objects.filter(email=form.data['username'])
            if not user or not user.check_password(form.data['password']):
                context['message'] = 'Неверное имя пользователя или пароль'
            else:
                login(request, user)
                return redirect('index')
    context['form'] = RegisterForm()
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')
