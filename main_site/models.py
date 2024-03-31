from django.db.models import Model, CharField, IntegerField, ForeignKey, ManyToManyField, CASCADE, ImageField, \
    BooleanField
from django.contrib.auth.models import AbstractUser


class BaseMethods:
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.filter(id=id).first()


class User(AbstractUser, BaseMethods):
    phone = CharField(max_length=20)
    teams = ManyToManyField('Team')
    tags = ManyToManyField('Tag')
    info = CharField(max_length=1024)
    votings = ManyToManyField('Idea')
    image = ImageField(upload_to='images/', default='images/default.jpg')

    @classmethod
    def get_by_username(cls, username):
        return User.objects.filter(username=username).first()

    @classmethod
    def get_by_email(cls, email):
        return User.objects.filter(email=email).first()


class Idea(Model, BaseMethods):
    name = CharField(max_length=265)
    description = CharField(max_length=1024)
    author = ForeignKey(to=User, on_delete=CASCADE, default=1)
    likes = IntegerField(default=0)
    dislikes = IntegerField(default=0)
    image = ImageField(upload_to='images/', default='images/idea.jpg')

    @classmethod
    def get_by_author(cls, author: 'User'):
        return Idea.objects.filter(author=author).all()


class Tag(Model, BaseMethods):
    name = CharField(max_length=64)
    ideas = ManyToManyField(Idea)


class Team(Model, BaseMethods):
    name = CharField(max_length=64)
    users = ManyToManyField(User)


class Request(Model, BaseMethods):
    # text = CharField(max_length=250)
    user_to = ForeignKey(to=User, on_delete=CASCADE, default=1, related_name='request_from')
    user_from = ForeignKey(to=User, on_delete=CASCADE, default=1, related_name='request_to')
    read = BooleanField(default=False)
    idea = ForeignKey(to=Idea, on_delete=CASCADE, default=1)