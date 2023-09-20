from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
    )
    list_editable = (
        'text',
        'author',
    )
    search_fields = (
        'text',
        'author',
    )
