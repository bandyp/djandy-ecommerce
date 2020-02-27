from django.forms import ModelForm, TextInput
from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'image', 'tag', 'published_date')