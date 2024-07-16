from django.db import models
import readtime

from .utils import markdown


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    rendered_content = models.TextField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    readtime = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.rendered_content = markdown(self.content)
        if not self.readtime:
            self.readtime = readtime.of_markdown(self.content).text
        super(BlogPost, self).save(*args, **kwargs)


class PinnedPost(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    cover = models.URLField()

    def __str__(self):
        return self.post.title
