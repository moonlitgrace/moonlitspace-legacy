from django.urls import path

from . import views

urlpatterns = [
    path("", views.newsletter_validate_view, name="newsletter_validate"),
]
