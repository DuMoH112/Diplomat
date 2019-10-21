# import packages/libs
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import imutils
import time
import cv2

# конструктор аргумнтов и их поиск
ap = argparse.ArgumentParser()
ap.add_argument('-o', '--output', type=str, default='result.csv')
args = vars(ap.parse_args())

# инициализация видеопотока
print('[INFO] starting stream')
vs = VideoStream(src=0).start()
time.sleep(2.0)

# открытие csv файла для записи и инициализации
csv = open(args["output"], "w")
found = set()

x = True
while x == True:
    # захват кадра из потокового видео и изменение его размера до 400px
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 0)

        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type

        # text = result
        text = '{}'.format(barcodeData)

        if barcodeData not in found:
            csv.write('{}\n'.format(barcodeData))
            csv.flush()
            found.clear()
            found.add(barcodeData)
            x = False

    cv2.imshow('QR Code scaner', frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break  # q to quit

print('[INFO] Cleaning up')
csv.close()
cv2.destroyAllWindows()
vs.stop()