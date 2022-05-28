from django.contrib import admin
from .models import Author, Category, Blog, Tag, EmailSignUp, \
    Contact, Comment, Reply


class CatAdmin(admin.ModelAdmin):
    list_display = ["name", "description", ]
    prepopulated_fields = {'slug': ('name',)}


class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = ["title", "category", "status", "visible", "get_author"]
    search_fields = ["title"]
    list_filter = ["category", "status", "visible"]


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ["name", "email", "subject"]
    search_fields = ["name", "email"]


admin.site.register(Category, CatAdmin)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(Comment)
# admin.site.register(Reply)
admin.site.register(Tag)
# admin.site.register(EmailSignUp)
admin.site.register(Contact, ContactAdmin)
