from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path("projects/<str:project_name>", views.ProjectsView.as_view(), name='project'),
]
