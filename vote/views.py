from django.contrib.auth.models import User
from django.http import request
from django.http.response import Http404, HttpResponse
from rest_framework.response import Response

# from rest_framework.views import APIView
# from .serializer import ProfileSerializer
from django.core.exceptions import ObjectDoesNotExist
from awards.settings import LOGOUT_REDIRECT_URL
from vote.models import Profile, Project
from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.


def logout_view(request):
    logout(request)


def index(request):
    try:
        projects = Project.objects.all()
    except ObjectDoesNotExist:
        raise Http404()

    context = {"projects": projects}

    return render(request, "index.html", context)
  
def rate(request):
  return 


def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise Http404()

    try:
        # remember to query and return projects for a particular user
        projects = Project.objects.all()
        noOfProjects = projects.count()
    except ObjectDoesNotExist:
        raise Http404()

    context = {"profile": profile, "projects": projects, "noOfProjects": noOfProjects}

    return render(request, "profile.html", context)


# method for all projects for a particular user
def projects(request):
    try:
        projects = Project.objects.all()
    except ObjectDoesNotExist:
        raise Http404()

    context = {"projects": projects}
    return render(request, "projects.html", context)


def rate(request, id):
  project = Project.objects.get(id=id)
  
  context = {
    'project' : project
  }

  return render(request, 'rate.html', context)