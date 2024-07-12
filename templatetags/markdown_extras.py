from django import template
from selectolax.parser import HTMLParser
import re

from utils.markdown import markdown

register = template.Library()


@register.filter
def markdown_to_text(md_string):
    html = markdown(md_string)

    tree = HTMLParser(html)
    # get only paragraphs tags text
    text = tree.css_first("p").text()
    # text = "\n".join([p.text() for p in p_tags])
    # remove code snippets
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return text
