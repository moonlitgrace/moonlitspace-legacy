import mistune
from mistune.renderers.markdown import MarkdownRenderer


markdown = mistune.create_markdown(renderer=mistune.HTMLRenderer())
