from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from authen.models import User
from fraternity.models import Team, Project
from .models import Post, Hashtag


class GetUserPosts(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return self.model.objects.filter(posted_by=user)


class GetTeamPosts(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_object(self):
        team = get_object_or_404(Team, slug=self.kwargs['team'])
        return self.model.objects.filter(team=team)


class GetProjectPosts(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_object(self):
        project = get_object_or_404(Project, slug=self.kwargs['project'])
        return self.model.objects.filter(project=project)


class GetHashtagPosts(DetailView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_object(self):
        hashtag = get_object_or_404(Hashtag, content=self.kwargs['hashtag'])
        return self.model.objects.filter(hashtags=hashtag)
