from django.conf.urls import url
from django.contrib import admin

from price import views

admin.autodiscover()

urlpatterns = [
    url(r'^price/', views.price, name='price'),
]
