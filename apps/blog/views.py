from django.views.generic.detail import DetailView

from .models import BlogPost


# Create your views here.
class BlogPostView(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "blog/detail.html"
