from django.forms import Form, CharField, Textarea, ImageField


class RegisterForm(Form):
    username = CharField(max_length=255, required=True)
    password = CharField(required=True)
    password_repeat = CharField(required=True)
    first_name = CharField(max_length=255, required=True)
    last_name = CharField(max_length=255, required=True)
    phone = CharField(max_length=20, required=False)
    info = CharField(max_length=1024, widget=Textarea(), required=False)
    image = ImageField()


class LoginForm(Form):
    username = CharField(required=True)
    password = CharField(required=True)


class IdeaForm(Form):
    name = CharField(max_length=255, required=True)
    description = CharField(max_length=1024, widget=Textarea(), required=False)
    image = ImageField()


class SetIdeaForm(Form):
    id = CharField(max_length=100, required=True)
    name = CharField(max_length=255, required=True)
    description = CharField(max_length=1024, required=True, widget=Textarea())
