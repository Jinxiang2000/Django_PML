from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('detail/<slug:pk>/', views.project_detail, name='project_detail'),
    path('create/', views.project_create_or_update, name='project_create'),
    path('update/<slug:pk>/', views.project_create_or_update, name='project_update'),
    path('delete/<slug:pk>/', views.project_delete, name='project_delete'),
    #Project Staff URL
    path('project-staff/', views.ProjectStaffListView.as_view(), name='project_staff_list'),
    path('project-staff/add/', views.ProjectStaffCreateView.as_view(), name='project_staff_add'),
    path('project-staff/<slug:pk>/edit/', views.ProjectStaffUpdateView.as_view(), name='project_staff_edit'),
    path('project-staff/<slug:pk>/delete/', views.ProjectStaffDeleteView.as_view(), name='project_staff_delete'),

    #Project Level Staff URL
    path('project/<slug:pk>/staff/', views.ProjectStaffManageView.as_view(), name='project_lvl_staff_manage'),
    path('project/<slug:project_pk>/staff/add/', views.ProjectStaffCreateView.as_view(), name='project_staff_add'),
    path('project/<slug:project_pk>/staff/<slug:pk>/edit/', views.ProjectStaffUpdateView.as_view(), name='project_staff_edit'),
    path('project/<slug:project_pk>/staff/<slug:pk>/delete/', views.ProjectStaffDeleteView.as_view(), name='project_staff_delete'),
]

