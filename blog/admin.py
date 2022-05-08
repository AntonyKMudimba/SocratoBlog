from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from blog.models import ArticleCategory, Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdAt', 'updatedAt')
    search_fields = ('name',)
    ordering = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'createdAt', 'updatedAt', 'isPublished')
    search_fields = ('title',)
    ordering = ['updatedAt', ]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.unregister(Group)
