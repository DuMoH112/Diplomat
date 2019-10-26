from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import ImageUploadForm
from .models import Card
from .actions_with_qr import *



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
                print(barcode_str)
                return render(request, 'ReadingQrCode/build/add_cart.html', {'barcode': barcode_str})
            else:
                context = 'Qr код не читается, попробуйте снова'
                return render(request, 'ReadingQrCode/build/Scan.html', {'req': context})
        else:
            context = 'Qr код не читается, попробуйте снова'
            return render(request, 'ReadingQrCode/build/Scan.html', {'req': context})
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
        card.last_name = barcode['last_name']
        card.first_name = barcode['first_name']
        card.patronymic = barcode['patronymic']
        card.number_phone = barcode['number_phone']
        card.e_mail = barcode['e_mail']
        card.address = barcode['address']
        card.company = barcode['company']
        card.position = barcode['position']
        card.web_site = barcode['web_site']
        # card.file = img
        card.save()
        return render(request, 'ReadingQrCode/build/my-cart.html', {'card': card})
    else:
        return render(request, 'ReadingQrCode/build/edit.html')


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

def add_card(request):
    card = Card()
    card.pk = Card.objects.count() + 2
    card.last_name = request.POST['last_name']
    card.first_name = request.POST['first_name']
    card.patronymic = request.POST['patronymic']
    card.number_phone = request.POST['number_phone']
    card.e_mail = request.POST['e_mail']
    card.address = request.POST['address']
    card.company = request.POST['company']
    card.position = request.POST['position']
    card.web_site = request.POST['web_site']
    card.save()
    card = Card.objects.all()
    return render(request, 'ReadingQrCode/build/menu.html')

def del_card(request):
    card = Card.objects.get(pk=request.POST['pk'])
    card.delete()
    card = Card.objects.all()
    return render(request, 'ReadingQrCode/build/contacts.html', {'card': card})