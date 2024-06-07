from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('detail/<slug:pk>/', views.project_detail, name='project_detail'),
    path('new/', views.project_create, name='project_create'),
    path('edit/<slug:pk>/', views.project_edit, name='project_edit'),
    path('delete/<slug:pk>/', views.project_delete, name='project_delete'),
    #Project Staff URL
    path('project-staff/', views.ProjectStaffListView.as_view(), name='project_staff_list'),
    path('project-staff/add/', views.ProjectStaffCreateView.as_view(), name='project_staff_add'),
    path('project-staff/<slug:pk>/edit/', views.ProjectStaffUpdateView.as_view(), name='project_staff_edit'),
    path('project-staff/<slug:pk>/delete/', views.ProjectStaffDeleteView.as_view(), name='project_staff_delete'),
]
