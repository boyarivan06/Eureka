from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from string import ascii_uppercase, ascii_lowercase, digits
from django.contrib.auth.decorators import login_required
from main_site.models import User, Idea, Request


@login_required
def add_like(request, id):
    obj = Idea.get_by_id(id)
    if obj not in request.user.votings.all():
        obj.likes += 1
        obj.save()
        request.user.votings.add(obj)
        return HttpResponse('Ok')
    return HttpResponseForbidden('можно голосовать только один раз')


@login_required
def add_dislike(request, id):
    obj = Idea.get_by_id(id)
    if obj not in request.user.votings.all():
        obj.dislikes += 1
        obj.save()
        request.user.votings.add(obj)
        return HttpResponse('Ok')
    return HttpResponseForbidden('можно голосовать только один раз')


@login_required
def delete_idea(request, id):
    idea = Idea.get_by_id(id)
    idea.delete()
    return HttpResponse(200)


def get_ideas(request):
    ideas = Idea.objects.all()
    data = {'ideas': [{'id': idea.id, 'description': idea.description,
                       'name': idea.name, 'author_id': idea.author.id,
                       'likes': idea.likes, 'dislikes': idea.dislikes} for idea in ideas]}
    print(data)
    return JsonResponse(data)


@login_required
def add_request(request):
    if request.method == 'POST':
        data = request.POST
        if not Request.objects.filter(user_from=User.get_by_id(data['user_from']),
                                      idea=Idea.get_by_id(data['idea_id'])):
            r = Request(user_from=User.get_by_id(data['user_from']),
                        idea=Idea.get_by_id(data['idea_id']))
            r.save()
            return JsonResponse({'id': r.idea.id})
        return HttpResponseForbidden('request exists')