from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as authlogout, login as authlogin, authenticate
from .models import Project
from .forms import UserForm

def index(request):
    return HttpResponseRedirect(reverse('projects:user_show', args=(request.user.id,)))

def login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            authlogin(request, user)
            return HttpResponseRedirect(reverse('projects:index'))
    return render(request, 'projects/login.html')

def logout(request):
    authlogout(request)
    return HttpResponseRedirect(reverse('projects:index'))

class UserList(generic.ListView):
    model = User
    template_name = 'projects/user_list.html'

class UserShow(generic.DetailView):
    model = User
    template_name = 'projects/user_show.html'

def UserCreate(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.is_staff = True
            new_user.save()
            return HttpResponseRedirect(reverse('projects:index'))
    else:
        form = UserForm()
    return render(request, 'projects/user_form.html', {'form': form})

class ProjectList(generic.ListView):
    model = Project
    template_name = 'projects/project_list.html'

class ProjectShow(generic.DetailView):
    model = Project
    template_name = 'projects/project_show.html'

class ProjectCreate(generic.edit.CreateView):
    model = Project
    fields = ['title', 'description']
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreate, self).form_valid(form)

def toggleInterest(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.user in project.interested.all():
        project.interested.remove(request.user)
    else:
        project.interested.add(request.user)
    project.save()
    return HttpResponseRedirect(reverse('projects:project_show', args=(project_id,)))

