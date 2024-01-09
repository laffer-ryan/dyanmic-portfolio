from django.db import models
from django.contrib.auth.models import User

# Create your models here

class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=400)
    age = models.IntegerField(null=True)
    university_degree = models.CharField(max_length=50) # These need to be changed to _id fields from here down
    academic_certifications = models.CharField(max_length=50)
    
    job_title = models.CharField(max_length=40, null=True, blank=True)
    activity = models.CharField(max_length=40, null=True, blank=True)
    career_goal = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user_id.username
    
class University(models.Model):
    university_name = models.CharField(max_length=50)
    
    
class TechnicalSkill(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    skill = models.CharField(max_length=40)
    skill_icon = models.ImageField(null=True, default = None)
    top_skill = models.BooleanField(default=True)
    
    def __str__(self):
        return self.skill

class AcademicDegree(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_designation = models.CharField(max_length=50)
    FieldOfStudy = models.CharField(max_length=40)
    Institution = models.ForeignKey(University, models.CASCADE)
    graduation_date = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.FieldOfStudy
    
class Occupation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=40)
    
class Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=40, null=True, blank=True)
    
class CareerGoal(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    career_goal = models.TextField(null=True, blank=True)
    