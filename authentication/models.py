# -*- encoding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class Author(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    bio = models.TextField()
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    isVerified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name

    def get_username(self):
        return self.username

    def is_author_verified(self):
        return self.isVerified
