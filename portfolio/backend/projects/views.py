from django.shortcuts import render, redirect
from .models import Project

# Create your views here.

def projectListView(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'projects/project_list.html', context=context)

def projectView(request, pk):
    project = Project.objects.all(id=pk)
    
    context = {
        'project': project
    }
    
    return render(request, 'projects/project.html', context=context)