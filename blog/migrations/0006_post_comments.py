# Generated by Django 4.2.4 on 2023-09-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_comments_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blog.comment', verbose_name='Коментарі'),
        ),
    ]