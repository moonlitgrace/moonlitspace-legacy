from django.shortcuts import render

from apps.user.models import Profile

def index(request):
    profile = Profile.objects.get(type="anonymous", active=True)

    context = {
        "profile": profile
    }
    return render(request, "index.html", context)
