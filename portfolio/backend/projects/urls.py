from django.urls import path
from . import views

urlpatterns = [
    path('', views.projectListView, name='projects-list'),
    path('project/<str:pk>/', views.projectView, name='project')
]