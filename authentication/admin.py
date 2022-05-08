# -*- encoding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib.admin import display

from authentication.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_author', 'isVerified', 'phone')
    search_fields = ('phone',)
    list_filter = ["isVerified"]

    @display(ordering='username', description='Author')
    def get_author(self, author):
        return author.user


admin.site.register(Author, AuthorAdmin)
