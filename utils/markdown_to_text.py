import markdown2
import re
from selectolax.parser import HTMLParser

from .markdown import markdown

def markdown_to_text(md_string):
    html = markdown(md_string)
    print(html)

    tree = HTMLParser(html)
    # get only paragraphs tags text
    text = tree.css_first("p").text()
    # text = "\n".join([p.text() for p in p_tags])
    # remove code snippets
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return text
