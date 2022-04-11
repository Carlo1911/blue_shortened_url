from django.contrib import admin

from .models import TransformerUrl

# admin.site.register(TransformerUrl)


@admin.register(TransformerUrl)
class TransformerUrlAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "url", "visited_count", "created_at")
    list_filter = ("created_at",)
    search_fields = ("slug", "url", "title")
