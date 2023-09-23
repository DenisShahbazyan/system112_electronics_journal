# Generated by Django 4.2.5 on 2023-09-22 20:34

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', django_ckeditor_5.fields.CKEditor5Field(help_text='Введите текст поста', verbose_name='текст поста')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='дата редактирования')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='название тега')),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
                'ordering': ['id'],
            },
        ),
    ]
