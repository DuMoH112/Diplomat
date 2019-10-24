from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    url(r'load_photo/', views.input_file, name='LoadPhoto'),
    url(r'contact/', views.contact, name='ReviewContact'),
    url(r'', views.index),
]
