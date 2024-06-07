from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Project
from .forms import ProjectForm

def home_view(request):
    return render(request, 'projects/home.html', {})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(reverse('project_list'))
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

#Project Staff View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ProjectStaff
from .forms import ProjectStaffForm

class ProjectStaffListView(ListView):
    model = ProjectStaff
    context_object_name = 'project_staff'
    template_name = 'projects/project_staff_list.html'

class ProjectStaffCreateView(CreateView):
    model = ProjectStaff
    form_class = ProjectStaffForm
    template_name = 'projects/project_staff_form.html'
    success_url = reverse_lazy('project_staff_list')

class ProjectStaffUpdateView(UpdateView):
    model = ProjectStaff
    form_class = ProjectStaffForm
    template_name = 'projects/project_staff_form.html'
    success_url = reverse_lazy('project_staff_list')

class ProjectStaffDeleteView(DeleteView):
    model = ProjectStaff
    context_object_name = 'project_staff'
    template_name = 'projects/project_staff_confirm_delete.html'
    success_url = reverse_lazy('project_staff_list')