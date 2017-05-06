from django.conf.urls import url
from django.contrib import admin
from login import views
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^', views.login, name='login')


]
