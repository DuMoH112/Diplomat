import cv2
from pyzbar import pyzbar

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from setuptools.command.upload import upload

from .forms import UploadFileForm
from .models import Card

def decode_qr_code(file):
    img = cv2.imread(file)

    inverted = cv2.inRange(img, (0, 0, 0), (200, 200, 255))
    if pyzbar.decode(inverted) == []:
        inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

    barcode = pyzbar.decode(inverted)
    return barcode[0].data


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            decode = decode_qr_code(request.FILES['file'])
            context = {'all_info': decode, 'form': form}
            return render_to_response('ReadingQrCode/index.html', context)
    else:
        form = UploadFileForm()
    return render_to_response('ReadingQrCode/index.html', {'form': form})

# def index(request):
#     return render(request, 'ReadingQrCode/index.html')