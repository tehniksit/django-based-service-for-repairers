from django.conf.urls import url
from django.contrib import admin


from get_parts import views

admin.autodiscover()

urlpatterns = [

    url(r'^get-parts/(?:(?P<part_id>\d+)/)?$', views.get_parts, name='get_parts'),


]
# /(?P<inform>\d)*