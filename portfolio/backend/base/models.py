from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here

class UserProfile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    
    SEX_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    about = models.TextField(max_length=1000, null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, default=OTHER, max_length=100)
    date_birth = models.DateField(blank=True, null=True)
    city = models.CharField(null=True, blank=True, max_length=100)
    suburb = models.CharField(null=True, blank=True, max_length=100)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    cover_letter = models.FileField(upload_to='resumes', null=True, blank=True)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    social_github = models.URLField(max_length=200, null=True, blank=True)
    social_linkedIn = models.URLField(max_length=200, null=True, blank=True)
    social_youtube = models.URLField(max_length=200, null=True, blank=True)
    social_website = models.URLField(max_length=200, null=True, blank=True)
    
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    date_created = models.DateTimeField(default = timezone.now)
    last_updated = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class University(models.Model):
    university_name = models.CharField(
        max_length=50,
        help_text="University or Institution that provided a qualification")
    
    def __str__(self):
        return self.university_name
    
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        
    
class AcademicDegree(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    degree_designation = models.CharField(
        max_length=50,
        help_text="The class of degree you attained or are in the process of attaining.")
    field_of_study = models.CharField(
        max_length=100,
        help_text="The broad degree field or the focus you wish to represent.")
    institution = models.ForeignKey(University, models.CASCADE)
    graduation_date = models.DateField(
        help_text="Date of graduation or expected graduation."
        )
    is_completed = models.BooleanField(default=False)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.field_of_study
    
    class Meta:
        ordering = ['-updated', '-created']
        
class TechnicalSkill(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    skill = models.CharField(
        max_length=40,
        help_text="This skill could be a language, framework or field specific skill")
    skill_icon = models.FileField(
        blank=True,
        null=True,
        default=None,
        upload_to='static/images',
        )
    top_skill = models.BooleanField(default=True)
    
    def __str__(self):
        return self.skill

    
class Occupation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=40, null=True, blank=True)
    company = models.CharField(max_length=100)

    is_current = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.job_title
    

class JobDescription(models.Model):
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    job_description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.occupation.job_title
    
class Accomplishment(models.Model):
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    accomplishment = models.TextField(
        null=True,
        blank=True,
        help_text="Projects finished, awards attained or things you are proud of.")   
    
    def __str__(self) -> str:
        return self.occupation.job_title
    
    
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text="This should represent a competitive or leisure activity you enjoy on your free time.")
    
    def __str__(self) -> str:
        return self.activity
    
    
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
    
class CareerGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    career_goal = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.career_goal
    