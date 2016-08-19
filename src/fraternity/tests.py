from django.test import TestCase

from authen.models import User
from .models import Project, Team


# Create your tests here.
class TestFraternity(TestCase):

    def test_project(self):
        project = Project(
            name='standups', repo_url='http://www.github.com/CuriousLearner/standups')
        project.save()

        projects = Project.objects.filter()

        self.assertEqual(len(projects), 1)

        project = projects[0]

        self.assertEqual(project.name, 'standups')
        self.assertEqual(project.repo_url,
                         'http://www.github.com/CuriousLearner/standups')

    def test_teams(self):
        project = Project(
            name='standups', repo_url='http://www.github.com/CuriousLearner/standups')
        project.save()
        user = User(username='sanyam', email='sanyam@sanyamkhurana.com')
        user.set_password('password')
        user.save()
        team = Team(name='backend-devs', slug='backend-devs')
        team.save()
        team.users.add(user)
        team.projects.add(project)

        teams = Team.objects.all()

        self.assertEqual(len(teams), 1)

        team = teams[0]

        self.assertEqual(team.name, 'backend-devs')
        self.assertEqual(team.slug, 'backend-devs')
        self.assertEqual(team.users.get(pk=user.pk), user)
        self.assertEqual(team.projects.get(pk=project.pk), project)
