from django.contrib import admin
from .models import Program, Staff, ProjectContracts, ProjectStaff, Contract, Project
# Register your models here.
admin.site.register(Program)
admin.site.register(Project)
admin.site.register(Staff)
admin.site.register(ProjectContracts)
admin.site.register(ProjectStaff)
admin.site.register(Contract)