from django.urls import path

from . import views

urlpatterns = [
    path("", views.newsletter_validate_view, name="newsletter_validate"),
    path("verify-email/<int:entry_id>/", views.newsletter_verify_view, name="newsletter_verify"),
]
