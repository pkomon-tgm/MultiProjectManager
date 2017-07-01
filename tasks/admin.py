from django.contrib import admin

from .models import Task, TaskState, TaskLabel


admin.site.register(Task)
admin.site.register(TaskState)
admin.site.register(TaskLabel)