from django.contrib.auth import get_user_model
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


User = get_user_model()


class Tag(models.Model):
    """Модель 'Теги' для постов.

    Validators:
        - Каждый тег должен быть уникальным.
        - Одиним тегом можно пометить пост только один раз.
    """
    name = models.CharField(
        max_length=255,
        verbose_name='название тега',
        unique=True,
    )
    slug = models.SlugField(
        max_length=20,
        verbose_name='слаг',
        unique=True,
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'slug'],
                name='unique_post_tag',
            )
        ]

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """Модель 'Посты'."""
    text = CKEditor5Field(
        verbose_name='текст поста',
        help_text='введите текст поста',
        config_name='extends',
    )
    pub_date = models.DateTimeField(
        verbose_name='дата публикации',
        auto_now_add=True,
    )
    edit_date = models.DateTimeField(
        verbose_name='дата редактирования',
        auto_now=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        related_name='posts',
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='теги',
        related_name='posts',
        blank=True,
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return str(self.pk)


class ActionLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='автор',
        related_name='actionlogs',
    )
    action = models.TextField(
        verbose_name='лог',
    )
    text = CKEditor5Field(
        verbose_name='текст поста',
        config_name='extends',
    )
    timestamp = models.DateTimeField(
        verbose_name='дата',
        auto_now_add=True,
    )
    post_id = models.PositiveIntegerField(
        verbose_name='id поста',
    )

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
