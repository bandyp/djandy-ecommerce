from django.conf.urls import url, include
from accounts.views import logout, login, registration
from accounts import url_reset


urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset)),
]

"""url(r'^(?P<pk>\d+)/$', user_profile, name="user_profile"),"""
"""url(r'^(?P<pk>\d+)/edit/$', edit_profile, name='edit_profile')"""