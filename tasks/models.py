from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from projects.models import Project


class TaskLabel(models.Model):
    name = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.name


class TaskState(models.Model):
    name = models.CharField(primary_key=True, max_length=25)

    def __str__(self):
        return self.name


class Task(models.Model):
    part_of = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    subtask_of = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(TaskState, default="pending")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    due_to = models.DateTimeField(null=True, blank=True, default=None)
    labels = models.ManyToManyField(TaskLabel)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def state_string(self):
        output = str(self.state).replace("_", " ")
        return output[0].upper() + output[1:]

    class Meta:
        unique_together = ("part_of", "id")
