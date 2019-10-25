from django.db import models


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    patronymic = models.CharField(max_length=50, blank=True)
    number_phone = models.CharField(max_length=11, blank=True)
    e_mail = models.CharField(max_length=80, blank=True)
    address = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    web_site = models.CharField(max_length=50, blank=True)
    file = models.ImageField(null=True, blank=True, upload_to='ReadingQrCode/static/img_qr')

    def __int__(self):
        return self.pk