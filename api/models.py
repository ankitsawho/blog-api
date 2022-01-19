from django.db import models


class Post(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    tags = models.CharField(max_length=300, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250, blank=True)
    intro = models.TextField(blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createdAt']


class Category(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name
