from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=30, verbose_name="Категорія")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural ="Категорії"

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="Хештег")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural ="Хештеги"

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads/blog/post')
    description = models.CharField(max_length=50)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", default=None, null=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural ="Зображення"

class PhotoProfile(models.Model):
    image = models.ImageField(upload_to='uploads/blog/profile')
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural ="Зображення"

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    # image = models.URLField(default="http://placehold.it/900x300")
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name="Хештеги")
    post_image = models.ManyToManyField(Photo, blank=True, verbose_name="Зображення")
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name="Коментарі", default=None, null=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural ="Пости"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = "Автор")
    date = models.DateTimeField(auto_now_add=True, verbose_name = "Дата")
    description = models.TextField(max_length=300, verbose_name = "Текст")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост", default=None, null=True)

    def __str__(self):
        return f"{self.author} - {self.date}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural ="Коментарі"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='uploads/blog/profile/', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name="Дата народження", help_text="Дата народження користувача")
    country = models.CharField(max_length=30, verbose_name="Країна", help_text="Країна проживання користувача")
    group = models.CharField(max_length=30, verbose_name="Група", help_text="Група, до якої належить користувач")
    comments_count = models.PositiveIntegerField(default=0, verbose_name="Кількість коментарів", help_text="Кількість коментарів, залишених користувачем")
    mat_count = models.PositiveIntegerField(default=0, verbose_name="Кількість матеріалів", help_text="Кількість матеріалів, які користувач завантажив")
    forum_count = models.PositiveIntegerField(default=0, verbose_name="Кількість записів на форумі", help_text="Кількість форумів, на яких користувач активний")
    post_count = models.PositiveIntegerField(default=0, verbose_name="Кількість постів", help_text="Кількість постів, створених користувачем")
    days_onsite = models.PositiveIntegerField(default=0, verbose_name="Дні на сайті", help_text="Загальна кількість днів, які користувач провів на сайті")
    reputation = models.IntegerField(default=0, verbose_name="Репутація", help_text="Репутація користувача на сайті")

    def __str__(self):
        return self.user










