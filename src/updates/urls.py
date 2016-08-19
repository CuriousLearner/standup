from django.conf.urls import url
from .views import GetUserPosts, GetTeamPosts, GetProjectPosts, GetHashtagPosts


urlpatterns = [
    url(r'^team/(?P<team>[\w-]+)/posts$',  GetTeamPosts.as_view(),
        name="teamposts"),
    url(r'^project/(?P<project>[\w-]+)/posts$', GetProjectPosts.as_view(),
        name="projectposts"),
    url(r'^(?P<username>[\w-]+)/posts$', GetUserPosts.as_view(),
        name="userposts"),
    url(r'^hashtag/(?P<hashtag>[\w-]+)/posts$', GetHashtagPosts.as_view(),
        name="hashtagsposts"),
]
