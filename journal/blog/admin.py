from django.contrib import admin

from .models import Post, Tag


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
    filter_horizontal = (
        'tags',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'slug',
    )
    list_editable = (
        'name',
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {
        "slug": ("name",)
    }
