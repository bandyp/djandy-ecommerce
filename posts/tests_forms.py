from django.test import TestCase
from .forms import BlogPostForm
from .models import Post


class TestPostForms(TestCase):
    def test_post_content(self):
        form = BlogPostForm({'Title': 'Title'})
        self.assertFalse(form.is_valid())
        print(form.errors['content'], ['This field is required.'])