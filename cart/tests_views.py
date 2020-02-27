from django.test import TestCase
from products.models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile

class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
        
