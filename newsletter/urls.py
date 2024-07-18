from django.urls import path

from . import views

urlpatterns = [
    path("", views.newsletter_validate_view, name="newsletter_validate"),
    path(
        "verification/<int:entry_id>",
        views.newsletter_verification_view,
        name="newsletter_verification",
    ),
]
