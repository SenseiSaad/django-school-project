from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=['title','description','tech_stack','github_link','live_link','image_url','created_at']
        