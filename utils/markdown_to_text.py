import markdown2
from selectolax.parser import HTMLParser

def markdown_to_text(md_string):
    html = markdown2.markdown(md_string)

    tree = HTMLParser(html)
    # get only paragraphs tags text
    p_tags = tree.css("p")
    text = "\n".join([p.text() for p in p_tags])
    return text
