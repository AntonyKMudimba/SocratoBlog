import uuid

from ckeditor.fields import RichTextField
from django.db import models
from dashboard.models import Author
from django.utils.html import format_html


# Category model
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=True)
    image = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Description')

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return str(self.name)

    # tags model


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    # Blog model


class Blog(models.Model):
    status = (
        ('active', 'active'),
        ('pending', 'pending')
    )

    title = models.CharField(max_length=200, null=True)
    detail = RichTextField()
    cover_image = models.ImageField(upload_to='images/media', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=20, choices=status, default='pending')
    # show_hide = models.CharField(max_length=5,choices=visibility, default='show')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Blog'

    def overview(self):
        short = self.detail[:30]
        return short

    def get_author(self):
        return f"{self.author.first_name} {self.author.last_name}"

    @property
    def image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url

    def __str__(self):
        return f"{self.title} | {self.author.author.username} | {self.category} | {self.status}"


# Comment Class
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} | {self.name} "


# Reply Class
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
    name = models.CharField(max_length=200, null=True, blank=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} | {self.name} |{self.created_at}"


# email marketing system 
class EmailSignUp(models.Model):
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name_plural = " User Emails"

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Name')
    email = models.EmailField(null=True)
    messages = models.TextField()
    subject = models.CharField(max_length=200, null=True, verbose_name='Subjects')

    def __str__(self):
        return f"{self.name} | {self.subject}"
