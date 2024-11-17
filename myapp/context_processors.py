# myapp/context_processors.py
from .models import Projects


def projects(request):
    projects = Projects.objects.all()  # Retrieve all projects
    return {'projects': projects}  # This will add 'projects' to every template's context