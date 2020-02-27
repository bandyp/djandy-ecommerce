from django.test import TestCase
from .apps import AccountsConfig
from django.apps import apps

class TestAccountsConfig(TestCase):
    
    def test_accounts(self):
        self.assertEqual("accounts", AccountsConfig.name)
        self.assertEqual("accounts", apps.get_app_config("accounts").name)
