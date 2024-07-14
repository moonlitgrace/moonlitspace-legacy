import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html
# plugins
from mistune.plugins.formatting import strikethrough
from mistune.plugins.table import table
from mistune.plugins.url import url
from mistune.plugins.task_lists import task_lists
from mistune.plugins.spoiler import spoiler


class CustomRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        if info:
            lexer = get_lexer_by_name(info, stripall=True)
            formatter = html.HtmlFormatter(cssclass="codehilite")
            return highlight(code, lexer, formatter)
        return "<pre><code>" + mistune.escape(code) + "</code></pre>"

plugins = [
    strikethrough,
    table,
    url,
    task_lists,
    spoiler,
]

markdown = mistune.Markdown(renderer=CustomRenderer(), plugins=plugins)
