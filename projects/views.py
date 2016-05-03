from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Project

def index(request):
    return HttpResponseRedirect(reverse('projects:user_show', args=(request.user.id,)))

class UserList(generic.ListView):
    model = User
    template_name = 'projects/user_list.html'

class UserShow(generic.DetailView):
    model = User
    template_name = 'projects/user_show.html'

class ProjectList(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectShow(generic.DetailView):
    model = Project
    template_name = 'projects/project_show.html'

