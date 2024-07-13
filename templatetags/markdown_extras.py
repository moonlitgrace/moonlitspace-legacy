from django import template
from django.template.defaultfilters import stringfilter
from selectolax.parser import HTMLParser
import re

from utils.markdown import markdown

register = template.Library()


@register.filter
@stringfilter
def markdown_to_text(md_str):
    html = markdown(md_str)

    tree = HTMLParser(html)
    # get only paragraphs tags text
    text = tree.css_first("p").text()
    # text = "\n".join([p.text() for p in p_tags])
    # remove code snippets
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return text

@register.filter
def markdown_text(md_str):
    return markdown(md_str)
