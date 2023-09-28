from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель 'Пользователи'."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        verbose_name='почта',
        unique=True,
    )
    username = models.CharField(
        verbose_name='логин',
        max_length=150,
        default=None,
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=150,
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150,
    )
    patronymic = models.CharField(
        verbose_name='отчество',
        max_length=150,
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['id']

    def __str__(self) -> str:
        return (
            self.last_name + ' ' +
            self.first_name[:1] + '.' +
            self.patronymic[:1] + '.'
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
