from django.contrib import admin

from .models import Post, Tag, ActionLog


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка дял постов."""
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
    """Админка дял тегов."""
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


@admin.register(ActionLog)
class ActionLogAdmin(admin.ModelAdmin):
    """Админка дял Логов."""
    list_display = (
        'pk',
        'user',
        'action',
        'timestamp',
        'post_id',
    )
    search_fields = (
        'post_id',
    )
