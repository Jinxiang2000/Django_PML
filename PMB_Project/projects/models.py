from django.db import models
from django.urls import reverse


class Program(models.Model):
    program_id = models.CharField(max_length=50, primary_key=True)
    program_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.program_name
    
# Create your models here.
class Project(models.Model):
    project_id = models.CharField(max_length=50, primary_key=True)
    parent_project = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subprojects')
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    activity_status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current_phase = models.CharField(max_length=255, blank=True, null=True)
    project_manager = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True, related_name='managed_projects')
    
    def __str__(self):
        return f'{self.project_id} - {self.title}'
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    

class Staff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bureau = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class ProjectStaff(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    class Meta:
        unique_together = ('project', 'staff', 'role')

    def __str__(self):
        return f'{self.staff.name} on {self.project.title} as {self.role}'


class Contract(models.Model):
    contract_no = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255,null=True, blank=True)
    prime_vendor = models.CharField(max_length=255,null=True, blank=True)
    contract_manager = models.CharField(max_length=255,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    contract_type = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.title

class ProjectContracts(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'contract')

    def __str__(self):
        return f'{self.project.title} contract {self.contract.title}'