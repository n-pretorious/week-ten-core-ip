from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from django.core.exceptions import ObjectDoesNotExist
from awards.settings import LOGOUT_REDIRECT_URL
from vote.models import Profile, Project, Rate
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
        # remember to query and return projects for a particular user
        projects = Project.objects.filter(profile=request.user)
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
  rating = Rate.objects.filter(project=project)

  if request.method == "POST":
  
    design = request.POST.get('design')
    usability = request.POST.get('usability')
    content = request.POST.get('content')
    
    scores = Rate(project = project, design = design, usability = usability, content = content, author = request.user)
    
    scores.save()
  
  context = {
    'project' : project,
    'rating' : rating
  }

  return render(request, 'rate.html', context)

class ProfileList(APIView):
    def get(self, request, format=None):
        allProfiles = Profile.objects.all()
        serializers = ProfileSerializer(allProfiles, many=True)
        return Response(serializers.data)
      
class ProjectList(APIView):
    def get(self, request, format=None):
        allProjects = Project.objects.all()
        serializers = ProjectSerializer(allProjects, many=True)
        return Response(serializers.data)