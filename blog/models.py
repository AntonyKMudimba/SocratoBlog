from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from authentication.models import Author


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_created=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    createdAt = models.DateTimeField(auto_created=True)
    updatedAt = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    coverImage = models.ImageField()
    content = RichTextField()
    isPublished = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(ArticleCategory)

    class Meta:
        ordering = ['updatedAt']

    def __str__(self):
        return self.title
