from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("newsletter/", include("apps.newsletter.urls")),
    path("blog/", include("apps.blog.urls")),
]
