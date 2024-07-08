from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PinnedPost(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    cover = models.URLField()
