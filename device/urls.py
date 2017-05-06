from django.conf.urls import url
from django.contrib import admin

from device import views

admin.autodiscover()

urlpatterns = [
    url(r'^device/', views.device, name='device'),


]
