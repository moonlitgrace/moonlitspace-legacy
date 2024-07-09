from django.contrib import admin

from .models import BlogPost, PinnedPost


class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

    search_fields = ("title",)

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(PinnedPost)
