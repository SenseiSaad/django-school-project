from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    descripton=models.TextField()
    tech_stack=models.CharField()
    github_link=models.URLField()
    live_link=models.URLField()
    image_url=models.URLField()
    craeted_at=models.DateTimeField(is_auto_now_add=True)
    

    def __str__(self):
        return self.title