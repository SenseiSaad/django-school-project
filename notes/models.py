from django.db import models

# Create your models here.
class Note(models.Model):
    Title=models.CharField(max_length=48)
    Date=models.DateField(auto_now_add=True)
    Content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Title