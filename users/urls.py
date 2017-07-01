from django.conf.urls import url

from users import views

app_name = "users"

urlpatterns = [
    url(r'^signin', views.SignInView.as_view(), name="signin"),
    url(r'^signout', views.user_signout, name="signout"),
    url(r'^signup', views.SignUpView.as_view(), name="signup"),
]