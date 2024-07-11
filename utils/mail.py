from django.core import mail
from django.template.loader import render_to_string


def send_moonlit_mail(
    subject: str,
    to_email: str,
    template_name: str,
    context: dict | None = None,
    error_template_name: str | None = None,
):
    html_template = render_to_string(template_name, context)

    with mail.get_connection() as connection:
        email = mail.EmailMessage(
            subject=subject,
            body=html_template,
            to=[to_email],
            connection=connection,
        )
        email.content_subtype = "html"
        email.send()
