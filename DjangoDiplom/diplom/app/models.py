from django.db import models
from django.urls import reverse


# создаем Модель Выпечек
class Bake(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.CharField(max_length=3)
    def __str__(self):
        return self.username
