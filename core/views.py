from django.shortcuts import render

from utils.markdown_to_text import markdown_to_text

from apps.user.models import Profile
from apps.blog.models import PinnedPost

def index(request):
    profile = Profile.objects.get(type="anonymous", active=True)
    pinned_posts = PinnedPost.objects.all()

    for post in pinned_posts:
        post.content = markdown_to_text(post.post.content)

    context = {
        "profile": profile,
        "pinned_posts": pinned_posts
    }
    return render(request, "index.html", context)
