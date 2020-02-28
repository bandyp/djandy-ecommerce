from django.conf.urls import url
from .views import view_cart, add_to_cart, cart_action

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^action/(?P<id>\d+)', cart_action, name='cart_action'),
]

