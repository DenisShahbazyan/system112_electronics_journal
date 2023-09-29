from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save

from .models import Post, ActionLog


@receiver(pre_delete, sender=Post)
def log_post_deletion(sender, instance, **kwargs):
    ActionLog(
        user=instance.author,
        action=(
            f'Пост с id={instance.pk} удален пользователем '
            f'{instance.author.get_full_name} в {timezone.now()}.'
        ),
        text=instance.text,
        post_id=instance.pk,
    ).save()


@receiver(post_save, sender=Post)
def log_post_create_edition(sender, instance, created, **kwargs):
    post = ActionLog(
        user=instance.author,
        text=instance.text,
        post_id=instance.pk,
    )
    if created:
        post.action = (
            f'Пост с id={instance.pk} создан пользователем '
            f'{instance.author.get_full_name} в {timezone.now()}.'
        )
    else:
        post.action = (
            f'Пост с id={instance.pk} изменен пользователем '
            f'{instance.author.get_full_name} в {timezone.now()}.'
        )
    post.save()
