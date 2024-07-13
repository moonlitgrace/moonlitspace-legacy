import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class CustomRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = html.HtmlFormatter(cssclass="codehilite")
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"

markdown = mistune.Markdown(renderer=CustomRenderer())
