from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from bs4 import BeautifulSoup

User = get_user_model()


class Post(models.Model):
    text = RichTextUploadingField(
        verbose_name='Текст поста',
        help_text='Введите текст поста',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

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
