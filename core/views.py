from django.shortcuts import render

from apps.user.models import Profile
from apps.blog.models import PinnedPost, BlogPost


def index(request):
    profile = Profile.objects.get(type="anonymous", active=True)
    pinned_posts = PinnedPost.objects.all()
    latest_posts = BlogPost.objects.all().exclude(pk__in=pinned_posts)

    context = {
        "profile": profile,
        "pinned_posts": pinned_posts,
        "latest_posts": latest_posts,
    }
    return render(request, "index.html", context)
