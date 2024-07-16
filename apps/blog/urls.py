from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog-view"),
    path("all/", views.BlogPostListView.as_view(), name="post-list-view"),
    path("<slug:slug>/", views.BlogPostView.as_view(), name="post-detail-view"),
]
