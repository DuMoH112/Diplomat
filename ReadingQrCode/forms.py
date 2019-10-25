from django import forms

from ReadingQrCode.models import Card


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select a file', help_text='max. 20 megabytes')
