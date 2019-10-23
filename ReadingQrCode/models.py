from django.db import models

class Card(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    number_phone = models.CharField(max_length=11)
    e_mail = models.CharField(max_length=80)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    web_site = models.CharField(max_length=50)

    def __str__(self):
        return self



