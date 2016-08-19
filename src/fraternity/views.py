from django.views.generic import ListView, DetailView

from .models import Team, Project

# Create your views here.


class TeamListView(ListView):
    model = Team
    template_name = 'team.html'
    context_object_name = 'teams'


class ProjectListView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'projects'


class TeamDetailView(DetailView):
    model = Team
    template_name = 'team_detail.html'
    context_object_name = 'team'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
