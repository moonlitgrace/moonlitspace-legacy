from django.shortcuts import render
from django.http import HttpResponse

from .models import NewsLetterEntry

# Create your views here.
def newsletter_validate_view(request):
    email = request.POST.get("email")
    if NewsLetterEntry.objects.filter(email=email).exists():
        return HttpResponse("EMail already exiss")

    return render(request, "newsletter/verification_email_send.html", {"email": email})
