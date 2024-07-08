from django.contrib import admin

from .models import BlogPost, PinnedPost


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(PinnedPost)
