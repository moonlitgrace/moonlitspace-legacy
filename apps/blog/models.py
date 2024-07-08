from django.db import models

# from django_prose_editor.fields import ProseEditorField
# from django_markdown.models import MarkdownField


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
