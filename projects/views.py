from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import Project

class IndexView(generic.TemplateView):
    template_name = 'projects/index.html'

class UserShow(generic.DetailView):
    model = User
    template_name = 'projects/user_show.html'

class ProjectShow(generic.DetailView):
    model = Project
    template_name = 'projects/project_show.html'

