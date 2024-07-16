from django.shortcuts import redirect


# index page not ready yet
def index(request):
    return redirect("blog-view")
