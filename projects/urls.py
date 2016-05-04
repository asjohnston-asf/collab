from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'projects'
urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'users/add/$', views.UserCreate, name='user_create'),
    url(r'users/(?P<pk>[0-9]+)/update/$', login_required(views.UserUpdate.as_view()), name='user_update'),
    url(r'users/(?P<pk>[0-9]+)/', login_required(views.UserShow.as_view()), name='user_show'),
    url(r'users/', login_required(views.UserList.as_view()), name='user_list'),
    url(r'projects/add/$', login_required(views.ProjectCreate.as_view()), name='project_create'),
    url(r'projects/(?P<pk>[0-9]+)/update/$', login_required(views.ProjectUpdate.as_view()), name='project_update'),
    url(r'projects/(?P<project_id>[0-9]+)/interested/', login_required(views.toggleInterest), name='interested'),
    url(r'projects/(?P<pk>[0-9]+)/', login_required(views.ProjectShow.as_view()), name='project_show'),
    url(r'projects/', login_required(views.ProjectList.as_view()), name='project_list'),
]

