from django.shortcuts import render
from .models import Card

def index(request):
    return render(request, 'ReadingQrCode/index.html')