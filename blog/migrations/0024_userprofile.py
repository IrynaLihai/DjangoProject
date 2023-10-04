# Generated by Django 4.2.4 on 2023-10-02 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0023_post_post_image_remove_post_image_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(help_text='Дата народження користувача', verbose_name='Дата народження')),
                ('country', models.CharField(help_text='Країна проживання користувача', max_length=30, verbose_name='Країна')),
                ('group', models.CharField(help_text='Група, до якої належить користувач', max_length=30, verbose_name='Група')),
                ('comments_count', models.PositiveIntegerField(default=0, help_text='Кількість коментарів, залишених користувачем', verbose_name='Кількість коментарів')),
                ('mat_count', models.PositiveIntegerField(default=0, help_text='Кількість матеріалів, які користувач завантажив', verbose_name='Кількість матеріалів')),
                ('forum_count', models.PositiveIntegerField(default=0, help_text='Кількість форумів, на яких користувач активний', verbose_name='Кількість записів на форумі')),
                ('post_count', models.PositiveIntegerField(default=0, help_text='Кількість постів, створених користувачем', verbose_name='Кількість постів')),
                ('days_onsite', models.PositiveIntegerField(default=0, help_text='Загальна кількість днів, які користувач провів на сайті', verbose_name='Дні на сайті')),
                ('reputation', models.IntegerField(default=0, help_text='Репутація користувача на сайті', verbose_name='Репутація')),
                ('avatar', models.ForeignKey(blank=True, help_text='Зображення профілю', null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.photoprofile', verbose_name='Фото профілю')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]