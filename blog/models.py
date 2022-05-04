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


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name blog: {self.name} Author: {self.author}'


class Post(models.Model):
    class Meta():
        ordering = ['-created']

    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    draft = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=None, null=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='post', null=True, default=None, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('demo:index')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, default=None, null=True)

    def __str__(self):
        return self.text[:20]
