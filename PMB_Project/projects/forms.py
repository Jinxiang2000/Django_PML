from django import forms
from .models import Project, ProjectStaff, ProjectContracts
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

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

'''
class ProjectLvlStaffForm(forms.ModelForm):
    class Meta:
        model = ProjectStaff
        fields = ['staff', 'role', 'project']
        widgets = {
            'project': forms.HiddenInput()  # Hide the project field
        }

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  # Get project from view
        super().__init__(*args, **kwargs)
        if project:
            self.fields['project'].initial = project  # Set initial project
'''

class ProjectLvlStaffForm(forms.ModelForm):    
    class Meta:
        model = ProjectStaff
        fields = ['staff', 'role', 'project']  # Assuming these are the fields you want to manage

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  # Extract the project, removing it from kwargs to avoid TypeError
        super(ProjectLvlStaffForm, self).__init__(*args, **kwargs)
        self.fields['project'].initial = project
        self.fields['project'].widget = forms.HiddenInput()      


class ProjectContractForm(forms.ModelForm):
    class Meta:
        model = ProjectContracts
        fields = ['project', 'contract']