from django.views.generic.detail import DetailView
from django.shortcuts import render

from apps.user.models import Profile
from .models import BlogPost, PinnedPost


# Create your views here.
def index(request):
    profile = Profile.objects.get(type="anonymous", active=True)
    pinned_posts = PinnedPost.objects.all()
    latest_posts = BlogPost.objects.all().exclude(pk__in=pinned_posts)

    context = {
        "profile": profile,
        "pinned_posts": pinned_posts,
        "latest_posts": latest_posts,
    }
    return render(request, "blog/index.html", context)

class BlogPostView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "blog/detail.html"
