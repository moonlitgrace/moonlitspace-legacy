from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.conf import settings

from .models import BlogPost


# Create your views here.
def index(request):
    recent_posts = BlogPost.objects.all().order_by("-created_at")[:2]
    posts = BlogPost.objects.all().exclude(pk__in=recent_posts)

    context = {
        "profile": settings.PROFILE,
        "recent_posts": recent_posts,
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


class BlogPostView(DetailView):
    model = BlogPost
    context_object_name = "post"


class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = "posts"
