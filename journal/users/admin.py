from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'first_name',
        'last_name',
        'patronymic',
        'email',
        'is_active',
    )
    list_editable = (
        'first_name',
        'last_name',
        'patronymic',
        'email',
        'is_active',
    )
    search_fields = (
        'first_name',
        'last_name',
        'patronymic',
        'email',
    )
