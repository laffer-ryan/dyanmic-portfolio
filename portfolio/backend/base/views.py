from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import UserProfile, CareerGoal, Occupation, Activity,TechnicalSkill

# Create your views here.

def home(request, pk):
    user = get_object_or_404(User, id=pk)
    userprofile = get_object_or_404(UserProfile, user=user)
    careergoals = CareerGoal.objects.filter(user=user)
    occupations = Occupation.objects.filter(user=user)
    activities = Activity.objects.filter(user=user)
    technical_skills = TechnicalSkill.objects.filter(user=user)
    
    # projects = Project.objects.all()
    
    context = {
        'user': user,
        'userprofile': userprofile,
        'careergoals': careergoals,
        'occupation': occupations,
        'activities': activities,
        'technical_skills': technical_skills,
    }
    return render(request, 'base/home.html', context=context)