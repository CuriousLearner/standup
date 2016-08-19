from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.auth_login, name="login"),
    url(r'^logout/$', views.auth_logout, name="logout"),
    url(r'^register/$', views.auth_register, name="register"),
]
