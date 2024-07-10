from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

from .models import NewsLetterEntry


# Create your views here.
def newsletter_validate_view(request):
    email = request.POST.get("email")

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
        reverse("newsletter_verification", kwargs={"entry_id": entry.entry_id})
    )
    context = {"verification_url": verification_url}
    template = get_template("email/newsletter_verification.html").render(context)

    subject = "[moonlitspace] - Email Verification"
    recipient_list = [email]

    send_mail(
        subject,
        None,
        None,
        recipient_list,
        fail_silently=False,
        html_message=template,
    )
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
