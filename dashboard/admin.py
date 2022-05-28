from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ["get_username", "email", "designation", "is_approved"]
    search_fields = ["email"]
    list_filter = ["is_approved", "designation"]


admin.site.register(Author, AuthorAdmin)
admin.site.disable_action('delete_selected')
admin.site.unregister(Group)

