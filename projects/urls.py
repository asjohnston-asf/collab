from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'projects'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'users/(?P<pk>[0-9]+)/', views.UserShow.as_view(), name='user_show'),
    url(r'projects/(?P<pk>[0-9]+)/', views.ProjectShow.as_view(), name='project_show'),
]

