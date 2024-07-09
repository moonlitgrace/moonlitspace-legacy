from django.shortcuts import render

from .models import NewsLetterEntry

# Create your views here.
def newsletter_validate_view(request):
    email = request.POST.get("email")
    if NewsLetterEntry.objects.filter(email=email).exists():
        return render(request, "newsletter/state.html", context={
            "title": "Oops!",
            "message": "Email already subscribed, please try another one.",
        })
    return render(request, "newsletter/verification_email_send.html", {"email": email})

def newsletter_verify_view(request, entry_id):
    try:
        entry = NewsLetterEntry.objects.get(entry_id=entry_id)
        entry.verified = True
        entry.save()
    except NewsLetterEntry.DoesNotExist:
        pass
