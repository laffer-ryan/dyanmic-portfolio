from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.
def home(request, pk):
    user = User.objects.get(id=pk)
    # projects = Project.objects.all()
    
    context = {
        'user': user,
    }
    return render(request, 'base/home.html', context=context)