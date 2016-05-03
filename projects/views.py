from django.shortcuts import get_object_or_404
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

def toggleInterest(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user in project.interested.all():
        project.interested.remove(request.user)
    else:
        project.interested.add(request.user)
    project.save()
    return HttpResponseRedirect(reverse('projects:project_show', args=(project_id,)))

