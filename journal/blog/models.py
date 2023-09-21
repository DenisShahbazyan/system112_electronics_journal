from bs4 import BeautifulSoup
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='название тега',
        unique=True,
    )

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['id']

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    text = CKEditor5Field(
        verbose_name='текст поста',
        help_text='Введите текст поста',
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
        return self.text[:15]


@receiver(pre_save, sender=Post)
def remove_img_styles(sender, instance, **kwargs):
    html_code = instance.text
    soup = BeautifulSoup(html_code, 'html.parser')
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        img_tag.attrs.pop('style', None)
    instance.text = str(soup)


pre_save.connect(remove_img_styles, sender=Post)
