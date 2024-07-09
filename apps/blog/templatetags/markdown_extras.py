from django import template

from utils.markdown_to_text import markdown_to_text as md_to_text

register = template.Library()

@register.filter
def markdown_to_text(text):
    return md_to_text(text)
