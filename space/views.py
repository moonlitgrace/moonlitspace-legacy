from django.shortcuts import redirect
from django_hosts.resolvers import reverse

# index page not ready yet
def index(request):
    return redirect(reverse("blog-view", host="blog"))
