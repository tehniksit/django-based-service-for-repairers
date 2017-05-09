from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('logout.urls')),
    url(r'^', include('device.urls')),
    url(r'^', include('parts.urls')),
    url(r'^', include('price.urls')),




)
