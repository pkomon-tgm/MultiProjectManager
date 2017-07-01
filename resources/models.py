from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from projects.models import Project


class Resource(models.Model):
    part_of = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=200)
    author = models.OneToOneField(User)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("part_of", "id")
