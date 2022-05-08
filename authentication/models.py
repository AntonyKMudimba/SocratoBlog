# -*- encoding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone = models.CharField(max_length=15)
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def username(self):
        return self.user.get_full_name()

    def is_verified(self):
        return self.isVerified
