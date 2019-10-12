import csv
import qrcode
import psycopg2


def dataInput():
    vizitka['last_name'] = input('Введите фамилию: ')
    vizitka['first_name'] = input('Введите имя: ')
    vizitka['patronymic'] = input('Введите отчество: ')
    vizitka['phone_number'] = input('Введите номер телефона(прим. +7-999-777-99-99): ')
    vizitka['e_mail'] = input('Введите e-mail: ')
    vizitka['company'] = input('Введите компанию: ')
    vizitka['position'] = input('Введите должность: ')
    vizitka['web_site'] = input('Введите веб-сайт: ')


connect = psycopg2.connect(
    database='Cards',
    user='postgres',
    password='09051945',
    host='127.0.0.1',
    port='5432'
)

cursor = connect.cursor()

print("Database opened successfully")

vizitka = {}
dataInput()

cursor.execute(
    "SELECT count(*) FROM cards;"
    "insert into cards(id, last_name, first_name, patronymic, phone_number, e_mail, company, position, web_site), values(count, vizitka['last_name'], vizitka['first_name'], vizitka['patronymic'],  vizitka['phone_number'], vizitka['phone_number'], vizitka['e_mail'], vizitka['company'], vizitka['position'], vizitka['web_site']);"
)

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

img = qr.make_image(fill_color="black", back_color="white")
img.save('img/qrCOOOODE.jpg')

connect.commit()
print("Record inserted successfully")

connect.close()
print("Database closed successfully")
