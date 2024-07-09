from django.shortcuts import render

from .models import NewsLetterEntry

# Create your views here.
def newsletter_validate_view(request):
    email = request.POST.get("email")
    if NewsLetterEntry.objects.filter(email=email).exists():
        return render(request, "newsletter/validation_failed.html")
    return render(request, "newsletter/verification_email_send.html", {"email": email})
