from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'projects/index.html'

class UserShow(generic.DetailView):
    model = User
    template_name = 'projects/user_show.html'

