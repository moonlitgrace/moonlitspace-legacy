import uuid
from django.http import HttpResponse
from django.template.loader import render_to_string


def generate_entry_id():
    return uuid.uuid4().int

def render_error_http_response(tempalte_name: str, context: dict[str, str]):
    error_html_content = render_to_string(tempalte_name, context)
    return HttpResponse(error_html_content)
