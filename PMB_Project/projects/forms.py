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


class ProjectLvlStaffForm(forms.ModelForm):
    class Meta:
        model = ProjectStaff
        fields = ['staff', 'role']  # Assuming 'project' is also a field but we handle it separately

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super(ProjectStaffForm, self).__init__(*args, **kwargs)
        if project:
            # Set project as initial value and disable the field if you do not want it changed.
            self.fields['project'].initial = project
            self.fields['project'].disabled = True  # This makes the field non-editable
            


class ProjectContractForm(forms.ModelForm):
    class Meta:
        model = ProjectContracts
        fields = ['project', 'contract']