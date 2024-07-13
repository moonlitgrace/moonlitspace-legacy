from django.urls import path

from . import views

urlpatterns = [
    path("<slug:slug>/", views.BlogPostView.as_view(), name="post-view"),
]
