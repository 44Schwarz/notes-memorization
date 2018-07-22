from django.contrib import admin

# Register your models here.
from .models import Label, Project, Note

admin.site.register(Label)
admin.site.register(Project)
admin.site.register(Note)
