import os

import cv2
import numpy as np
import qrcode
from PIL import Image
from pyzbar import pyzbar

from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render

from .forms import ImageUploadForm, TextUploadForm
from .models import Card


def create_qr_code(barcode):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=12,
        border=1
    )


    qr.add_data(barcode)
    qr.make(fit=True)
    path = 'ReadingQrCode/static/img_qr/my_qr.jpg'
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    return path


def decode_qr_code(file):
    pic = Image.open(file)
    pic = pic.convert("L")
    pic = np.asarray(pic)
    pix = Image.fromarray(pic)
    pix.save('ReadingQrCode/static/images/tmp.jpeg')
    img = cv2.imread('ReadingQrCode/static/images/tmp.jpeg')

    inverted = cv2.inRange(img, (0, 0, 0), (200, 200, 255))
    if pyzbar.decode(inverted) == []:
        inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)
    barcode = pyzbar.decode(inverted)

    os.remove("ReadingQrCode/static/images/tmp.jpeg")
    return barcode[0].data

@csrf_protect
def input_file(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_multipart():
            try:
                barcode = decode_qr_code(request.FILES['button-load-file'])
            except:
                return render(request, 'ReadingQrCode/build/Scan.html')
            if barcode != []:
                barcode = str(barcode.decode('utf-8'))
                barcode_str = {
                    'last_name': barcode[barcode.find('last_name')+13:barcode.find('first_name')-4],
                    'first_name': barcode[barcode.find('first_name')+14:barcode.find('patronymic')-4],
                    'patronymic': barcode[barcode.find('patronymic')+14:barcode.find('number_phone')-4],
                    'number_phone': barcode[barcode.find('number_phone')+16:barcode.find('e_mail')-4],
                    'e_mail': barcode[barcode.find('e_mail')+10:barcode.rfind('address')-4],
                    'address': barcode[barcode.rfind('address')+11:barcode.find('company')-4],
                    'company': barcode[barcode.find('company')+11:barcode.find('position')-4],
                    'position': barcode[barcode.find('position')+12:barcode.find('web_site')-4],
                    'web_site': barcode[barcode.find('web_site')+12:barcode.find('END')-4],
                }

                return render(request, 'ReadingQrCode/build/add_cart.html', {'barcode': barcode_str, 'q':barcode})
            else:
                context = 'Qr код не читается, попробуйте снова'
                return render(request, 'ReadingQrCode/build/Scan.html', {'req': context})
        else:
            context = 'Qr код не читается, попробуйте снова'
            return render(request, 'ReadingQrCode/build/Scan.html', {'req': context})
        # return HttpResponseRedirect('ReadingQrCode/build/Scan.html', {'img': barcode})
    else:
        form = ImageUploadForm()
    return render(request, 'ReadingQrCode/build/Scan.html', {'img': form})


@csrf_protect
def save(request, pk=2):
    if request.method == 'POST':
        barcode = {
            'BEGIN': 'CARD',
            'last_name': '',
            'first_name': '',
            'patronymic': '',
            'number_phone': '',
            'e_mail': '',
            'address': '',
            'company': '',
            'position': '',
            'web_site': '',
            'END': 'CARD',
        }
        for bar in barcode:
            key = bar
            try:
                if request.POST[key]:
                    barcode[key] = request.POST[key]
            except:
                pass
        img = create_qr_code(barcode)
        card = Card.objects.get(pk=pk)
        card.last_name = barcode['last_name'],
        card.first_name = barcode['first_name'],
        card.patronymic = barcode['patronymic'],
        card.number_phone = barcode['number_phone'],
        card.e_mail = barcode['e_mail'],
        card.address = barcode['address'],
        card.company = barcode['company'],
        card.position = barcode['position'],
        card.web_site = barcode['web_site'],
        card.file = img,
        card.save()
        return render(request, 'ReadingQrCode/build/my-cart.html')
    else:
        form = TextUploadForm()
    return HttpResponse(request, 'ReadingQrCode/build/edit.html', {'form': form})
    # form = TextUploadForm(requset.POST)


def index(request):
    return render(request, 'ReadingQrCode/build/menu.html')


def scan(request):
    return render(request, 'ReadingQrCode/build/scan.html')


def catalog(request):
    card = Card.objects.all()
    return render(request, 'ReadingQrCode/build/contacts.html', {'card': card})


def my_cart(request):
    card = Card.objects.get(pk=2)
    return render(request, 'ReadingQrCode/build/my-cart.html', {'card': card})


def edit(request):
    card = Card.objects.get(pk=2)
    return render(request, 'ReadingQrCode/build/edit.html', {'card': card})


def card(request, pk=2):
    card = Card.objects.get(pk=pk)
    return render(request, 'ReadingQrCode/build/cart.html', {'card': card})
