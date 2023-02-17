from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'categoryType', 'postCategory', 'text']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        name = cleaned_data.get("title")
        if name == text:
            raise ValidationError(
                "Текст не должен быть идентичен названию."
            )
        return cleaned_data

    def clean_title(self):
        name = self.cleaned_data["title"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name