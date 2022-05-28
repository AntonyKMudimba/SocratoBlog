from ckeditor.widgets import CKEditorWidget
from django import forms

from blog.models import Blog
from dashboard.models import Author


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=300)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = ('title', 'content', 'cover_image', 'category',)


class AuthorForm(forms.ModelForm):
    about = forms.CharField(widget=forms.Textarea(), required=True, max_length=800)

    class Meta:
        model = Author
        fields = (
            'email', 'first_name', 'last_name', 'phone', 'author_image', 'twitter', 'facebook', 'instagram', 'about')
