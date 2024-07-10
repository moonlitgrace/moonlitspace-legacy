from apps.newsletter.forms import NewsLetterEntryFrom


def newsletter_form_processor(request):
    form = NewsLetterEntryFrom
    return {"newsletter_form": form}
