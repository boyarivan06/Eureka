from django.forms import Form, CharField


class RegisterForm(Form):
    username = CharField(max_length=255, required=True)
    password = CharField(required=True)
    password_repeat = CharField(required=True)
    first_name = CharField(max_length=255, required=True)
    last_name = CharField(max_length=255, required=True)
    phone = CharField(max_length=20, required=False)


class LoginForm(Form):
    username = CharField(required=True)
    password = CharField(required=True)


class IdeaForm(Form):
    name = CharField(max_length=255, required=True)
    description = CharField(max_length=1000, required=True)
