from django.conf.urls import url
from django.contrib import admin

from parts import views

admin.autodiscover()

urlpatterns = [
    url(r'^parts/', views.parts, name='parts'),
]
