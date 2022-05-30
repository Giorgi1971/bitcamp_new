from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from sqlalchemy import null
from user.models import Author
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField(max_length=124, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    describtion = models.TextField(blank=True)
    cat_image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.category_name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='post')

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, default="anonymous")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post", pk=self.post.pk)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_date']
