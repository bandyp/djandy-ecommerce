from django.test import TestCase
from .forms import (UserLoginForm, UserRegistrationForm)
from django.contrib.auth.models import User

class TestAccountsForms(TestCase):
    def test_login_password_required(self):
        form = UserLoginForm({'username': 'admin'})
        self.assertFalse(form.is_valid())
        print(form.errors['password'], ['This field is required.'])
        
    def test_login_username_required(self):
        form = UserLoginForm({'password': 'dfghj'})
        self.assertFalse(form.is_valid())
        print(form.errors['username'], ['This field is required.'])