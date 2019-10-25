from django.conf.urls import url

from ReadingQrCode.views import *
from django.urls import path, re_path

urlpatterns = [
    url(r'save/', save, name='SaveData'),
    url(r'edit/', edit, name='EditMyCard'),
    url(r'card/(?P<pk>[0-9]+)/', card, name='ViewCard'),
    url(r'scanned_code/', input_file, name='LoadPhoto'),
    url(r'my-card/', my_cart, name='MyCard'),
    url(r'catalog/', catalog, name='Catalog'),
    url(r'scan/', scan, name='Scan'),
    url(r'', index, name='Menu'),
]
