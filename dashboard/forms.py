from ckeditor.widgets import CKEditorWidget
from django import forms

from blog.models import Blog


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=300)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = ('title', 'content', 'cover_image', 'category',)
