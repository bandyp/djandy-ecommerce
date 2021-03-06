
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from accounts import urls as urls_accounts
from accounts.views import logout, login, registration
from home.views import about
from home.views import index
from products import urls as urls_products
from cart import urls as urls_cart
from contact import urls as urls_contact
from posts import urls as urls_posts
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^about/', about, name='about'),
    url(r'^home/', index, name='index'),
    url(r'^contact/', include(urls_contact)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^posts/', include(urls_posts)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
