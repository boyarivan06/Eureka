from django.db.models import Model, CharField, IntegerField, ForeignKey, ManyToManyField, CASCADE
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = CharField(max_length=20)
    teams = ManyToManyField('Team')
    tags = ManyToManyField('Tag')
    info = CharField(max_length=1024)


class Idea(Model):
    name = CharField(max_length=265)
    description = CharField(max_length=1024)
    author = ForeignKey(to=User, on_delete=CASCADE, default=1)
    likes = IntegerField(default=0)
    dislikes = IntegerField(default=0)


class Tag(Model):
    name = CharField(max_length=64)
    ideas = ManyToManyField(Idea)


class Team(Model):
    name = CharField(max_length=64)
    users = ManyToManyField(User)
