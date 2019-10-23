import qrcode
import psycopg2
from psycopg2 import sql
from contextlib import closing

userID = 0

def dataInput():
     vizitkaS['last_name'] = input('Введите фамилию: ')
     vizitkaS['first_name'] = input('Введите имя: ')
     vizitkaS['patronymic'] = input('Введите отчество: ')
     vizitkaS['phone_number'] = input('Введите номер телефона(прим. +7-999-777-99-99): ')
     vizitkaS['e_mail'] = input('Введите e-mail: ')
     vizitkaS['company'] = input('Введите компанию: ')
     vizitkaS['position'] = input('Введите должность: ')
     vizitkaS['web_site'] = input('Введите веб-сайт: ')


vizitkaS = {}
dataInput()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=12,
    border=1
)

vizitka = []
with closing(psycopg2.connect(
        database='Cards',
        user='postgres',
        password='09051945',
        host='127.0.0.1',
        port='5432'
)) as connect:
    print("Database opened successfully")
    with connect.cursor() as cursor:
        connect.autocommit = True

        insert = sql.SQL('insert INTO cards (id, last_name, first_name, patronymic, number_phone,'
                         ' e_mail, company, position, web_site) VALUES {}').format(sql.SQL(',').join())
        data = cursor.fetchall()

    print("Record inserted successfully")
print("Database closed successfully")
print(vizitka[0])


qr.add_data(vizitka[0][6:-1:])
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('img/qrCOOOODE.jpg')
