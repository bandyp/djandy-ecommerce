from django.test import TestCase
from .models import Order, OrderLineItem

class TestCheckoutModels(TestCase):

    def test_place_order_products(self):
        order_line_item = OrderLineItem()
        self.assertFalse(order_line_item.quantity)