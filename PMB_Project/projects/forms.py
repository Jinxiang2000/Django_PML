from django import forms
from .models import Project, ProjectStaff, ProjectContracts

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_id', 'parent_project', 'program', 'title', 'activity_status', 'start_date', 'end_date', 'current_phase', 'project_manager']
        widgets = {
            'start_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'end_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }

class ProjectStaffForm(forms.ModelForm):
    class Meta:
        model = ProjectStaff
        fields = ['project', 'staff', 'role']


class ProjectContractForm(forms.ModelForm):
    class Meta:
        model = ProjectContracts
        fields = ['project', 'contract']