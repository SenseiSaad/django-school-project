from rest_framework import serializers
from .models import Note


class NoteSetializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=['Title','Date','Content' , 'created_at']