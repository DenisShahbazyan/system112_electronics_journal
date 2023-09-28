from django.contrib.auth.hashers import make_password
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для пользователей."""
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

    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
