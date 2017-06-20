from django.conf.urls import url
from django.contrib import admin

from landing import views

admin.autodiscover()

urlpatterns = [
    url(r'^landing/(?:(?P<sort_id>\d+)/)?$', views.landing, name='landing'),

]
