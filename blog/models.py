from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='post', null=True, default=None)

    def get_absolute_url(self):
        return reverse('demo:index')


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=None, null=True)

    def __str__(self):
        return self.text[:20]
