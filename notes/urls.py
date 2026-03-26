from django.urls import path
from . import views


urlpatterns = [
path('create/' , views.adanote, name='add-note'),
path('all/' , views.allnotes, name='all-notes'),
path('update/<str:pk>/' , views.updatenote, name='update-note'),
path('delete/<str:pk>/' , views.deletenote, name='delete-note'),
path('<str:pk>/' , views.getnote, name='get-note'),


]