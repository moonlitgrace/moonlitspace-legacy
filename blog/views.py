from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render

from user.models import Profile
from .models import BlogPost, PinnedPost


# Create your views here.
def index(request):
    profile = Profile.objects.filter(type="anonymous", active=True).first()
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


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = "posts"
