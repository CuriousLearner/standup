from __future__ import unicode_literals

from django.db import models
from authen.models import User


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60)
    repo_url = models.URLField()
    description = models.CharField(max_length=500)
    slug = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=60)
    slug = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    projects = models.ManyToManyField(Project)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
