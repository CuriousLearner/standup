from __future__ import unicode_literals

from django.db import models
from authen.models import User
from fraternity.models import Project, Team

# Create your models here.


class Hashtag(models.Model):
    content = models.CharField(max_length=20)

    def __str__(self):
        return self.content


class Comment(models.Model):
    content = models.CharField(max_length=200)
    posted_on = models.DateTimeField()
    posted_by = models.ForeignKey(User)

    def __str__(self):
        return self.content


class Post(models.Model):
    content = models.CharField(max_length=500)
    posted_on = models.DateTimeField()
    modified_on = models.DateTimeField()
    posted_by = models.ForeignKey(User)
    comments = models.ManyToManyField(Comment, blank=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    project = models.ForeignKey(Project)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.content
