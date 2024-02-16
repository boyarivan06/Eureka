from django.contrib.auth import login, logout
from django.http import JsonResponse, HttpResponse
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
    return HttpResponse(200)


@login_required
def add_dislike(request, id):
    obj = Idea.objects.filter(id=id).first()
    if obj not in request.user.votings.all():
        obj.dislikes += 1
        obj.save()
        request.user.votings.add(obj)
    return HttpResponse(200)


@login_required
def delete_idea(request, id):
    idea = Idea.objects.filter(id=id).first()
    idea.delete()
    return HttpResponse(200)
