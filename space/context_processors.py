from newsletter.forms import NewsLetterEntryFrom


def newsletter_form(request):
    form = NewsLetterEntryFrom
    return {"newsletter_form": form}
