# Generated by Django 4.2.5 on 2023-09-28 21:52

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(help_text='введите текст поста', verbose_name='текст поста'),
        ),
    ]