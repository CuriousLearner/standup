from django.conf.urls import url
from .views import TeamListView, ProjectListView, TeamDetailView, ProjectDetailView


urlpatterns = [
    url(r'^team/$', TeamListView.as_view(), name="teamlist"),
    url(r'^project/$', ProjectListView.as_view(), name="projectlist"),
    url(r'^team/(?P<slug>[\w-]+)$', TeamDetailView.as_view(),
        name="teamdetail"),
    url(r'^project/(?P<slug>[\w-]+)$', ProjectDetailView.as_view(),
        name="projectdetail"),
]
