from django.conf.urls import url, include
from .views import all_products, earrings, rings, harmony_bells, bracelets, necklaces

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', earrings, name='earrings'),
    url(r'^$', rings, name='rings'),
    url(r'^$', harmony_bells, name='harmony_bells'),
    url(r'^$', bracelets, name='bracelets'),
    url(r'^$', necklaces, name='necklaces'),
    ]