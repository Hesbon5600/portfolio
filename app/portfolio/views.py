import json

# from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.base import View

from .models import Project, Client


def error_404(request, *args, **kwargs):
        data = {}
        return render(request,'404.html', data)

def error_500(request,  *args, **kwargs):
        data = {}
        return render(request,'500.html', data)
class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"


class WorkHistoryView(TemplateView):
    template_name = "work-history.html"

    def get(self, request):
        clients = Client.objects.filter(deleted=False).all()
        return render(request, self.template_name, context={"data": clients})

class ProjectsView(TemplateView):
    template_name = "projects.html"

    def get(self, request):
        projects = Project.objects.filter(deleted=False).all()
        return render(request, self.template_name, context={"data": projects})


class ProjectView(View):
    template_name = "single-project.html"

    def get(self, request, project_name):
        project = Project.objects.get(slug__iexact=project_name)
        return render(request, self.template_name, context={"data": project})
