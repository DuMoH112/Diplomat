import os

import cv2
import numpy as np
from PIL import Image
from django.conf.global_settings import MEDIA_ROOT
from django.template.context_processors import csrf
from pyzbar import pyzbar

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from setuptools.command.upload import upload

from .forms import ImageUploadForm
from .models import Card

def decode_qr_code(file):
    pic = Image.open(file)
    pix = np.array(pic)
    pix = Image.fromarray(pix)
    pix.save('ReadingQrCode/static/images/tmp.jpg')
    img = cv2.imread('ReadingQrCode/static/images/tmp.jpg')

    inverted = cv2.inRange(img, (0, 0, 0), (200, 200, 255))
    if pyzbar.decode(inverted) == []:
        inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
    barcode = pyzbar.decode(inverted)

    os.remove("ReadingQrCode/static/images/tmp.jpg")
    return barcode

def index(request):
    return render(request,'ReadingQrCode/build/index.html')

def input_file(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_multipart():
            barcode = decode_qr_code(request.FILES['button-load-file'])
            if barcode != []:
                return render(request, 'ReadingQrCode/build/contacts.html', barcode)
            else:
                context = 'Qr код не читается, попробуйте снова'
                return render(request,'ReadingQrCode/build/ErrorQr.html', {'img': context})
        else:
            return HttpResponse('Invalid image')
        # return HttpResponseRedirect('ReadingQrCode/build/index.html', {'img': barcode})
    else:
        form = ImageUploadForm()
    return render(request, 'ReadingQrCode/build/index.html', {'img': form})

def contact(request):
    return HttpResponse('ReadingQrCode')