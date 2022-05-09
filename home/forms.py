from ckeditor.widgets import CKEditorWidget
from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=300)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = ('title', 'content',)
