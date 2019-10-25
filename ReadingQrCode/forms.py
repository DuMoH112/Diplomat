from django import forms

from ReadingQrCode.models import Card


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select a file', help_text='max. 20 megabytes')

class TextUploadForm(forms.Form):
    last_name = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    patronymic = forms.CharField(max_length=50)
    number_phone = forms.CharField(max_length=11)
    e_mail = forms.CharField(max_length=80)
    address = forms.CharField(max_length=50)
    company = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)
    web_site = forms.CharField(max_length=50)
    class Meta:
        model = Card