from django.contrib import admin
from .models import Post, Category, Comment, Tag, Photo, PhotoProfile
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Photo)
admin.site.register(PhotoProfile)
