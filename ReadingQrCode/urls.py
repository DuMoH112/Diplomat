from django.conf.urls import url

from ReadingQrCode.views import *
from django.urls import path, re_path

urlpatterns = [
    url('save/$', save, name='SaveData'),
    url('del/$', del_card, name='DelData'),
    url('edit/$', edit, name='EditMyCard'),
    url('add-card/$', add_card, name='AddNewCard'),
    url('card/(?P<pk>[0-9]+)/$', card, name='ViewCard'),
    url('scanned_code/$', input_file, name='LoadPhoto'),
    url('my-card/$', my_cart, name='MyCard'),
    url('catalog/$', catalog, name='Catalog'),
    url('scan/$', scan, name='Scan'),
    url('', index, name='Menu'),
]
