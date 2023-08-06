from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'postCategory', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title is not None and len(title) > 140:
            raise ValidationError({
                "title": "Title can't be longer than 140 characters"
            })
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'postCategory', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title is not None and len(title) > 140:
            raise ValidationError({
                "title": "Title can't be longer than 140 characters"
            })
        return cleaned_data
