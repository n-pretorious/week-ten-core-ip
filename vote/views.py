from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from awards.settings import LOGOUT_REDIRECT_URL
from vote.models import Profile
from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request, "index.html")


def profile(request):
    try:
        profile = Profile.objects.get(user = request.user)
        print(profile)
    except ObjectDoesNotExist:
        raise Http404()

    context = {
      'profile': profile
    }
    return render(request, "profile.html", context)

    # else:
    #   return HttpResponse('not found')


def logout_view(request):
    logout(request)