from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    url(r'/input-file', views.input_file, name='input-file'),
    url(r'/Submit', views.Sub, name='Submit'),
]
