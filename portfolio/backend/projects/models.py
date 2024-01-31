from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(
        null=True,
        default="output.png",
        help_text="This picture demonstrates a visualization that was a result of your machine learning application"
    )
    project_description = models.TextField(max_length=1000, null=True, blank=True)
    github_link = models.URLField(max_length=400, null=True, blank=True)
    other_link = models.URLField(max_length=400, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    