from django.conf.urls import url
from django.contrib import admin
from logout import views


admin.autodiscover()

urlpatterns = [

    url(r'^logout/$', views.logout_view, name='logout')


]
