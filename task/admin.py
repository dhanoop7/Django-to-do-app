from django.contrib import admin
from .models import CustomUser, Task

admin.site.register(CustomUser)
admin.site.register(Task)


