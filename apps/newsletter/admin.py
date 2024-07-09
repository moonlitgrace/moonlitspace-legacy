from django.contrib import admin

from .models import NewsLetterEntry

class NewsLetterEntryAdmin(admin.ModelAdmin):
    list_display = ("email", "verified")
    search_fields = ("email", )
    readonly_fields = ("entry_id", "verified")
    list_filter = ("verified", )

    fieldsets = (
        (None, {"fields": ("email", "entry_id", "verified")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": ("email", )
        }),
    )

# Register your models here.
admin.site.register(NewsLetterEntry, NewsLetterEntryAdmin)
