from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from string import ascii_uppercase, ascii_lowercase, digits
from django.contrib.auth.decorators import login_required
from main_site.forms import RegisterForm, LoginForm, IdeaForm
from main_site.models import User, Idea


def password_is_valid(raw_password):
    return len(raw_password) >= 8 and (set(raw_password) & set(ascii_uppercase)) \
           and (set(raw_password) & set(ascii_lowercase)) and (set(raw_password) & set(digits))


def index_view(request):
    context = {
        'user': request.user,
        'ideas': Idea.objects.all()
    }

    return render(request, 'index.html', context)


def registration_view(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                context['message'] = f'Пароли не совпадают'
            elif not password_is_valid(form.cleaned_data['password']):
                context['message'] = f'Пароль ненадёжен'
            elif not form.cleaned_data['email']:
                context['message'] = 'Введите электронную почту'
            else:
                user = User(username=form.cleaned_data['username'].lower(),
                               first_name=form.cleaned_data['first_name'],
                               last_name=form.cleaned_data['last_name'],
                               email=form.cleaned_data['email'].lower( )
                               )
                user.set_password(form.cleaned_data['password'])
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
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if not user:
                user = User.objects.filter(email=form.cleaned_data['username'])
            if not user or not user.check_password(form.cleaned_data['password']):
                context['message'] = 'Неверное имя пользователя или пароль'
            else:
                login(request, user)
                return redirect('index')
    context['form'] = RegisterForm()
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def new_idea_view(request):
    context = dict()
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = Idea(name=form.cleaned_data['name'], description=form.cleaned_data['description'],
                        author=request.user)
            idea.save()
            return redirect('index')
    context['form'] = IdeaForm()
    return render(request, 'new_idea.html', context)


@login_required
def profile_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'profile.html', context)
