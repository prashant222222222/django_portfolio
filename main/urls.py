
from django.urls import path

from main import views

urlpatterns=[
path('projects/', views.projects, name= 'projects'),
path('skills/', views.skills, name= 'skills'),
path('',views.index, name= 'index'),
]
