from django.core import mail
from django.template.loader import render_to_string
from typing import Union, Optional

def send_moonlit_mail(
    subject: str,
    recipient_list: Union[list[str], str],
    template_name: str,
    context: Optional[dict] = None,
    error_template_name: Optional[str] = None,
):
    """ check if recipient list is a list
    or not - conver to a list """
    if not isinstance(recipient_list, list):
        recipient_list = list(recipient_list)

    html_template = render_to_string(template_name, context)

    with mail.get_connection() as connection:
        email = mail.EmailMessage(
            subject=subject,
            body=html_template,
            to=recipient_list,
            connection=connection,
        )
        email.content_subtype = "html"
        email.send()
