from django.contrib import admin
from .models import Team, Project


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields]


class ProjectAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Project._meta.fields]


# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Project, ProjectAdmin)
