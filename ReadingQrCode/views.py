import cv2
from django.template.context_processors import csrf
from pyzbar import pyzbar

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from setuptools.command.upload import upload

# from .forms import UploadFileForm
from .models import Card

def decode_qr_code(file):
    img = cv2.imread(file)

    inverted = cv2.inRange(img, (0, 0, 0), (200, 200, 255))
    if pyzbar.decode(inverted) == []:
        inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

    barcode = pyzbar.decode(inverted)
    return barcode[0].data

def index(request):
    return render(request,'ReadingQrCode/build/index.html')

def input_file(request):
    if request.method == 'POST':
        barcode = decode_qr_code(request.FILES('file'))
        if barcode.is_valid:
            csv = open('../1/result.csv', 'w', newline='')
            csv.write('{}\n'.format(barcode))
            csv.close()
            return HttpResponse("YYYEEEEESSSS")
        else:
            barcode = decode_qr_code()
    return render(request, 'ReadingQrCode\index.html', {'img': barcode})


def Sub(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('ReadingQrCode\h1.html', c)