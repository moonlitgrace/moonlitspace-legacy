from django.shortcuts import render, redirect
from django_hosts.resolvers import reverse

from .utils import send_mail
from .models import NewsLetterEntry


# Create your views here.
def newsletter_validate_view(request):
    email = request.POST.get("email")
    if email is None:
        return redirect(reverse("home", host="www"))

    if NewsLetterEntry.objects.filter(email=email).exists():
        return render(
            request,
            "newsletter/state.html",
            context={
                "title": "Oops!",
                "message": "Email already subscribed, please try another one.",
            },
        )
    # create new entry
    entry = NewsLetterEntry.objects.create(email=email)

    verification_url = request.build_absolute_uri(
        reverse("newsletter_verification", kwargs={"entry_id": entry.entry_id}, host="newsletter")
    )
    template_name = "newsletter/mail/newsletter_verification.html"
    error_template_name = "newsletter/state.html"
    context = {"verification_url": verification_url}
    subject = "[moonlitspace] - Email Verification"

    success, error_response = send_mail(
        subject, email, template_name, context, error_template_name
    )
    if not success:
        return error_response
    return render(request, "newsletter/verification_email_send.html", {"email": email})


def newsletter_verification_view(request, entry_id):
    try:
        entry = NewsLetterEntry.objects.get(entry_id=entry_id)
        if not entry.verified:
            entry.verified = True
            entry.save()

        return render(
            request,
            "newsletter/state.html",
            context={
                "title": "Woohoo!",
                "message": "Verification completed successfully! from now you'll get updates via email.",
            },
        )
    except NewsLetterEntry.DoesNotExist:
        return render(
            request,
            "newsletter/state.html",
            context={
                "title": "Oh no!",
                "message": "Email entry not found, please follow the steps shown on the verification email that we've sended before. Or try again.",
            },
        )
