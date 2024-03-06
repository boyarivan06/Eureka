from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from string import ascii_uppercase, ascii_lowercase, digits
from django.contrib.auth.decorators import login_required
from main_site.models import User, Idea


@login_required
def add_like(request, id):
    obj = Idea.objects.filter(id=id).first()
    if obj not in request.user.votings.all():
        obj.likes += 1
        obj.save()
        request.user.votings.add(obj)
        return HttpResponse('Ok')
    return HttpResponseForbidden('можно голосовать только один раз')


@login_required
def add_dislike(request, id):
    obj = Idea.objects.filter(id=id).first()
    if obj not in request.user.votings.all():
        obj.dislikes += 1
        obj.save()
        request.user.votings.add(obj)
        return HttpResponse('Ok')
    return HttpResponseForbidden('можно голосовать только один раз')


@login_required
def delete_idea(request, id):
    idea = Idea.objects.filter(id=id).first()
    idea.delete()
    return HttpResponse(200)


def get_ideas(request):
    ideas = Idea.objects.all()
    data = {'ideas': [{'id': idea.id, 'description':idea.description,
                       'name': idea.name, 'author_id': idea.author.id,
                       'likes': idea.likes, 'dislikes': idea.dislikes} for idea in ideas]}
    print(data)
    return JsonResponse(data)


def api_login(request):
    if request.method == 'POST':
        print('post on api login')
        data = request.POST
        login = data['login']
        password = data['password']
        print(login, password)

    else:
        print('get on api login')
        return HttpResponse(status=200)
