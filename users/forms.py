from django.forms import Form, CharField, EmailField, PasswordInput
from django.contrib.auth.models import User


class SigninForm(Form):
    username = CharField(label="Username", max_length=20)
    password = CharField(widget=PasswordInput, label="Password", max_length=50)


class SignupForm(Form):
    username = CharField(label="Username", max_length=20, min_length=4, required=True)
    email = EmailField(label="E-mail address", max_length=75)
    first_name = CharField(label="First name", max_length=50)
    last_name = CharField(label="Last name", max_length=50)
    password = CharField(widget=PasswordInput, label="Password", max_length=50, min_length=8)
    password_repeat = CharField(widget=PasswordInput, label="Password (repeat)", max_length=50,
                                min_length=8)

    def clean(self):
        super(Form, self).clean()
        form_data = self.cleaned_data
        pw = form_data.get("password")
        pw_repeat = form_data.get("password_repeat")
        if pw and pw_repeat and pw != pw_repeat:
            self.add_error("password", "")
            self.add_error("password_repeat", "Passwords do not match.")
        if User.objects.filter(username=form_data.get("username")).exists():
            self.add_error("username", "Username already in use.")
        if User.objects.filter(email=form_data.get("email")).exists():
            self.add_error("email", "Email already in use.")
        return form_data
