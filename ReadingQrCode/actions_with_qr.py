import os

import cv2
import numpy as np
import qrcode
from PIL import Image
from pyzbar import pyzbar


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
