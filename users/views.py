from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from users.forms import SigninForm, SignupForm


@login_required
def user_signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))


class SignInView(View):
    def get(self, request):
        if request.user.is_authenticated:  # is already logged in
            return HttpResponseRedirect(reverse("internal:overview"))
        else:
            form = SigninForm()
            return render(request, "users/signin.html", {"form": form})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is None:  # failed auth
            form = SigninForm()
            return render(request, "users/signin.html", {"err": True, "form": form})
        else:  # success
            login(request, user)
            return HttpResponseRedirect(reverse("internal:overview"))


class SignUpView(View):
    def get(self, request):
        if request.user.is_authenticated:  # is already logged in
            return HttpResponseRedirect(reverse("internal:overview"))
        else:
            form = SignupForm()
            return render(request, "users/signup.html", {"form": form})

    def post(self, request):
        register_form = SignupForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            email = register_form.cleaned_data["email"]
            first_name = register_form.cleaned_data["first_name"]
            last_name = register_form.cleaned_data["last_name"]
            password = register_form.cleaned_data["password"]
            new = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name,
                                      password=password)
            new.save()
            login(request, new)
            return HttpResponseRedirect(reverse("internal:overview"))
        return render(request, "users/signup.html", {"form": register_form})
