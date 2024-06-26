from django.forms import Form, CharField, Textarea, \
    ImageField, EmailField, PasswordInput, EmailInput


class RegisterForm(Form):
    username = CharField(max_length=255, required=True)
    password = CharField(required=True, widget=PasswordInput())
    password_repeat = CharField(required=True, widget=PasswordInput())
    email = EmailField(required=True, widget=EmailInput)
    first_name = CharField(max_length=255, required=True)
    last_name = CharField(max_length=255, required=True)
    phone = CharField(max_length=20, required=False)
    info = CharField(max_length=1024, widget=Textarea(), required=False)
    image = ImageField()


class LoginForm(Form):
    username = CharField(required=True)
    password = CharField(required=True, widget=PasswordInput())


class IdeaForm(Form):
    name = CharField(max_length=255, required=True)
    description = CharField(max_length=1024, widget=Textarea(), required=False)
    image = ImageField()


class SetIdeaForm(Form):
    id = CharField(max_length=100, required=True)
    name = CharField(max_length=255, required=True)
    description = CharField(max_length=1024, required=True, widget=Textarea())
