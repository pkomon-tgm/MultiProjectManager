import logging
import sys

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import Project

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))


def index(request):
    return HttpResponse("Hello, world!")


@login_required
def overview(request):
    user = request.user
    projects = user.project_set.all()
    for p in projects:
        __get_project_stats(p)
    return render(request, "projects/overview.html", {"projects": projects})


def project_detail(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return HttpResponseNotFound()

    __get_project_stats(project)

    return render(request, "projects/detail_view.html", {"project": project})


def __get_project_stats(project):
    if not isinstance(project, Project):
        raise TypeError("'project' must be of type internal.models.Project")

    project.task_count_total = project.task_set.count()
    project.task_count_completed = project.task_set.filter(state="complete").count()
    project.task_count_pending = project.task_count_total - project.task_count_completed

    if project.task_count_total != 0:
        project.percent_completed = project.task_count_completed / project.task_count_total * 100
    else:
        project.percent_completed = 0.0
