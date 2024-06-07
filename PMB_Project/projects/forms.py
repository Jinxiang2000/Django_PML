from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_id', 'parent_project', 'program', 'title', 'activity_status', 'start_date', 'end_date', 'current_phase', 'project_manager']
        widgets = {
            'start_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'end_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }
