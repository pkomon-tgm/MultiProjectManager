from django.conf.urls import url, include

from projects import views

app_name = "projects"

urlpatterns = [
    url(r'^/', views.overview, name="overview"),
    url(r'^(?P<id>[0-9]+)/', views.project_detail, name="project_detail"),
]
