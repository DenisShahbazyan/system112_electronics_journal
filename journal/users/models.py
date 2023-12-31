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
        return f'{self.last_name} {self.first_name[:1]}. {self.patronymic[:1]}.'

    def save(self, *args, **kwargs):
        if self.email:
            self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    @property
    def get_full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.patronymic}'
