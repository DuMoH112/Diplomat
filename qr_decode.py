from pyzbar import pyzbar
import cv2
import argparse

file = input('Укажите путь к файлу\n')

img = cv2.imread(file)

inverted = cv2.inRange(img, (0, 0, 0), (200, 200, 255))
if pyzbar.decode(inverted) == []:
    inverted = 255 - cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

barcode = pyzbar.decode(inverted)
csv = open('result.csv', 'w', newline='')
csv.write('{}\n'.format(barcode))
csv.close()

print(barcode[0].data)