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

def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'project': project})

'''
def project_create_or_update(request, pk=None):
    if pk:
        project = get_object_or_404(Project, pk=pk)
        form = ProjectForm(request.POST or None, instance=project)
    else:
        form = ProjectForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('project_list')

    return render(request, 'projects/project_form.html', {'form': form})



def project_create_or_update(request, pk=None):
    if pk:  # If an ID is provided, this should be an update operation
        project = get_object_or_404(Project, pk=pk)
        if request.method == 'POST':
            form = ProjectForm(request.POST, instance=project)  # Pass instance for updating
            if form.is_valid():
                form.save()
                return redirect('project_list')
        else:
            form = ProjectForm(instance=project)
    else:  # No ID provided, treat as a new project
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('project_list')
        else:
            form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form})

'''
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect(reverse('project_list'))
    return render(request, 'projects/project_confirm_delete.html', {'project': project})

#Project Staff View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ProjectStaff
from .forms import ProjectStaffForm,ProjectLvlStaffForm

class ProjectStaffListView(ListView):
    model = ProjectStaff
    context_object_name = 'project_staff'
    template_name = 'projects/project_staff_list.html'

#Project Level Staff List
class ProjectStaffManageView(ListView):
    model = ProjectStaff
    template_name = 'projects/project_lvl_staff_list.html'
    context_object_name = 'project_staff'

    def get_queryset(self):
        """
        This method enhances the queryset by ensuring that it not only filters by project_id
        but also selects related data to prevent multiple database hits per row when accessing related fields.
        """
        return ProjectStaff.objects.filter(project_id=self.kwargs['pk']).select_related('staff')

    def get_context_data(self, **kwargs):
        """
        Adds the project to the context data, ensuring the template can display details about the project
        alongside the staff information.
        """
        context = super().get_context_data(**kwargs)
        # Safely get the project object with handling for DoesNotExist
        context['project'] = get_object_or_404(Project, pk=self.kwargs['pk'])
        return context
    
class ProjectLvlStaffCreateView(CreateView):
    model = ProjectStaff
    form_class = ProjectLvlStaffForm
    template_name = 'projects/project_staff_form.html'
   

    def get_form_kwargs(self):
        kwargs = super(ProjectStaffCreateView, self).get_form_kwargs()
        project = self.kwargs.get('project_pk')  # Assuming you capture 'project_pk' from the URL
        if project:
            kwargs['instance'] = ProjectStaff(project=project)
        return kwargs

    def get_success_url(self):
        return reverse('project_lvl_staff_manage', kwargs={'pk': self.object.project.pk})

class ProjectLvlStaffUpdateView(UpdateView):
    model = ProjectStaff
    form_class = ProjectLvlStaffForm
    template_name = 'projects/project_staff_form.html'
    

    def get_form_kwargs(self):
        kwargs = super(ProjectStaffCreateView, self).get_form_kwargs()
        project = self.kwargs.get('project_pk')  # Assuming you capture 'project_pk' from the URL
        if project:
            kwargs['instance'] = ProjectStaff(project=project)
        return kwargs

    def get_success_url(self):
        return reverse('project_lvl_staff_manage', kwargs={'pk': self.object.project.pk})

class ProjectLvlStaffDeleteView(DeleteView):
    model = ProjectStaff
    context_object_name = 'project_staff'
    template_name = 'projects/project_staff_confirm_delete.html'
    

    def get_success_url(self):
        return reverse('project_lvl_staff_manage', kwargs={'pk': self.kwargs['project_pk']})

    
#Overall Project Staff List
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