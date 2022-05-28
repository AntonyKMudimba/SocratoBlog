from django.db import models
from django.contrib.auth.models import User


# author model
class Author(models.Model):
    roles = (
        ('editor', 'editor'),
        ('author', 'author')
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Name')
    designation = models.CharField(max_length=20, choices=roles, default='author')
    author_image = models.ImageField(upload_to='author/', verbose_name='Author Profile Image', blank=True, null=True)
    is_approved = models.BooleanField(null=True, default=False)
    twitter = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    about = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=15, null=True)

    class Meta:
        verbose_name_plural = 'Author'

    def __str__(self):
        return self.author.username

    def get_username(self):
        return f"{self.first_name} {self.last_name}"

    def get_twitter(self):
        if self.twitter == "" or self.twitter is None:
            return f"{self.author.username}"
        else:
            return f"{self.twitter}"

    def get_facebook(self):
        if self.facebook == "" or self.facebook is None:
            return f"{self.author.username}"
        else:
            return f"{self.facebook}"

    def get_instagram(self):
        if self.instagram == "" or self.instagram is None:
            return f"{self.author.username}"
        else:
            return f"{self.instagram}"

    def get_about(self):
        if self.about == "" or self.about is None:
            return ""
        else:
            return self.about
