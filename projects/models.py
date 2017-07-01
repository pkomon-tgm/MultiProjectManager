from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(unique=True, max_length=100)
    desc = models.CharField(max_length=500)
    icon_path = models.CharField(max_length=100)
    participants = models.ManyToManyField(User)
    created_on = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return self.name
