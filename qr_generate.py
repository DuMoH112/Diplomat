import csv
import qrcode

#qrImg = qrcode.make(csv)
#qrImg.save('qr.png')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=1
)

with open('result.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]

qr.add_data(data_read[0])
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
img.save('qrCOOOODE.jpg')
