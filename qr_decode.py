from pyzbar import pyzbar
from pyzbar.pyzbar import decode
from PIL import Image
import argparse
import imutils
import cv2

file = 'qr2.png' #input('Укажите путь к файлу\n')

img = cv2.imread(file)


#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted = cv2.inRange(img,(0,0,0),(200,200,255))
if pyzbar.decode(inverted) == []:
    inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

height, width = 300, 300
resize = imutils.resize(inverted, height=height, width=width)

barcode = pyzbar.decode(inverted)

print(barcode)





cv2.imshow('Width', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

