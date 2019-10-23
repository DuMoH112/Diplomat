import psycopg2
from contextlib import closing

vizitkas = []
with closing(psycopg2.connect(
        database='Cards',
        user='postgres',
        password='09051945',
        host='127.0.0.1',
        port='5432'
)) as connect:
    print("Database opened successfully")
    with connect.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM cards;"
        )
        data = cursor.fetchall()

        for row in data:
            vizitkas += [
                'ID:' + str(row[0]) + ' ' + str([
                    'BEGIN:CARD',
                    'NAME: ' + str(row[1]) + '; ' + str(row[2]) + '; ' + str(row[3]) + ';',
                    'TEL: ' + str(row[4]) + ';',
                    'EMAIL: ' + str(row[5]) + ';',
                    'COMPANY: ' + str(row[6]) + ';',
                    'POSITION: ' + str(row[7]) + ';',
                    'URL: ' + str(row[8]) + ';',
                    'END:CARD'
                ]),
            ]
    print("Record inserted successfully")
print("Database closed successfully")
for vizitka in vizitkas:
    print(vizitka)
    print()