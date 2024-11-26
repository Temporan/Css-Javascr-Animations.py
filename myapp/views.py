from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from . import models
from .models import Projects
from django.shortcuts import get_object_or_404


# Create your views here.
class ProjectsView(TemplateView):
    def get_template_names(self):
        # Capture the project name 'name' from the URL
        project_name = self.kwargs.get('project_name').casefold()

        # Map project_name to specific template |v-2|
        template_map = {
            f'project_{i}': f'myapp/project_{i}.html' for i in range(1, Projects.objects.count() + 1)
        }

        # Map project_name to specific template |v-1|
        # template_map = {
        #     'project_1': 'myapp/project_1.html',
        #     'project_2': 'myapp/project_2.html',
        #     'project_3': 'myapp/project_3.html',
        #     'project_4': 'myapp/project_4.html',
        #     'project_5': 'myapp/project_5.html',
        #     'project_6': 'myapp/project_6.html',
        #     'project_7': 'myapp/project_7.html',
        #     'project_8': 'myapp/project_8.html',
        #     'project_9': 'myapp/project_9.html',
        #     'project_10': 'myapp/project_10.html',
        #     # Add more mappings for each project as needed
        # }


        # Return the appropriate template or a default one
        return [template_map.get(project_name, 'myapp/default.html')]

    def get_context_data(self, **kwargs):
        # Fetch base context data
        context = super().get_context_data(**kwargs)

        # Retrieve the current project
        project_name = self.kwargs.get('project_name').casefold()
        current_project = get_object_or_404(Projects, name__iexact=project_name)

        # Add current project to context
        context['project'] = current_project

        # Fetch all projects for navigation
        projects = list(Projects.objects.order_by('id'))
        current_index = projects.index(current_project)

        # Determine next and previous projects
        context['next_project'] = projects[current_index + 1] if current_index + 1 < len(projects) else None
        context['previous_project'] = projects[current_index - 1] if current_index - 1 >= 0 else None

        return context
