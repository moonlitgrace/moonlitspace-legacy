from django.core.mail import get_connection, EmailMessage, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from typing import Union, Optional


def send_moonlit_mail(
    subject: str,
    recipient_list: Union[list[str], str],
    template_name: str,
    context: Optional[dict] = None,
    error_template_name: Optional[str] = None,
):
    if not isinstance(recipient_list, list):
        """ check if recipient list is a list, if not - convert to a list """
        recipient_list = list(recipient_list)

    html_template = render_to_string(template_name, context)

    try:
        with get_connection() as connection:
            email = EmailMessage(
                subject=subject,
                body=html_template,
                to=recipient_list,
                connection=connection,
            )
            email.content_subtype = "html"
            email.send()

        return True, None
    except BadHeaderError:
        context = {
            "title": "Oh no!",
            "message": "Invalid header found"
        }
        if error_template_name:
            error_response = render_to_string(error_template_name, context)
            return False, HttpResponse(error_response)
        else:
            return False, None
    except Exception as e:
        if settings.DEBUG:
            print(e)
        """ handle other possible exceptions """
        context = {
            "title": "Oops!",
            "message": "Something went wrong, please re-check email and try again."
        }
        if error_template_name:
            error_response = render_to_string(error_template_name, context)
            return False, HttpResponse(error_response)
        else:
            return False, None
