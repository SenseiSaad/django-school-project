from django.urls import path
from . import views



urlpatterns = [
    path('view_all/', views.view_all_projects, name='view_all_projects'),
    path('create/', views.create_project, name='create_project'),
    path('view_one/<int:pk>/', views.view_projects, name='view_projects'),
    path('update/<int:pk>/', views.update_project, name='update_project'),
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),
]