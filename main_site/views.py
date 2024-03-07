from django.contrib.auth import login, logout
# from django.http import JsonResponse
from django.shortcuts import render, redirect
from string import ascii_uppercase, ascii_lowercase, digits
from django.contrib.auth.decorators import login_required
from main_site.forms import RegisterForm, LoginForm, IdeaForm, SetIdeaForm
from main_site.models import User, Idea


def password_is_valid(raw_password):
    return len(raw_password) >= 8 and (set(raw_password) & set(ascii_uppercase)) \
           and (set(raw_password) & set(ascii_lowercase)) and (set(raw_password) & set(digits))


def index_view(request):
    context = {
        'user': request.user,
        'ideas': Idea.get_all()[::-1]
    }

    return render(request, 'index.html', context)


def registration_view(request):
    context = {}
    if request.method == 'POST':
        print('catch post')
        form = RegisterForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            print('form is valid')
            if form.data['password'] != form.data['password_repeat']:
                context['message'] = f'Пароли не совпадают'
            elif not password_is_valid(form.data['password']):
                context['message'] = f'Пароль ненадёжен'
            else:
                user = User(username=form.data['username'].lower(),
                            first_name=form.data['first_name'],
                            last_name=form.data['last_name'],
                            email=form.data['email'].lower(),
                            image=form.files['image']
                            )
                user.set_password(form.data['password'])
                user.save()
                login(request, user)
                return redirect('index')
        else:
            context['message'] = 'form is not valid !!'
    else:
        form = RegisterForm()
    context['form'] = form
    return render(request, "reg.html", context)


def login_view(request):
    context = {}
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():

            user = User.get_by_username(form.data['username'])
            if not user:
                user = User.get_by_email(form.data['email'])
            if not user or not user.check_password(form.data['password']):
                context['message'] = 'Неверное имя пользователя или пароль'
            else:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def new_idea_view(request):
    context = dict()
    context['form'] = IdeaForm()
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = Idea(name=form.data['name'],
                        description=form.data['description'],
                        author=request.user,
                        image=form.files['image'])
            idea.save()
            return redirect('index')
        context['form'] = form
    return render(request, 'new_idea.html', context)


@login_required
def profile_view(request):
    if request.method == 'POST':
        if request.POST['action_type'] == 'set_idea':
            form = SetIdeaForm(request.POST)
            if form.is_valid():
                idea = Idea.get_by_id(form.data['id'])
                idea.name = form.data['name']
                idea.description = form.data['description']
                idea.save()
    context = {
        'user': request.user,
        'ideas': Idea.get_by_author(request.user)[::-1]
    }
    return render(request, 'profile.html', context)
