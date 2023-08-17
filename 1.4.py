import csv
import psycopg2

try:
    #Подключение к бд
    connection =  psycopg2.connect(user = 'postgres',
                                   password = 'serg328328',
                                   host = 'localhost',
                                   port = '5432',
                                   database = 'net_py1')
    cursor = connection.cursor()

    oper_date = '2018-01-10'

    cursor.execute('set search_path to dm')
    cursor.callproc('db_cr_date', (oper_date,))
    headers = [desc[0] for desc in cursor.description]



    with open(f'C:/neostudy/1.4/1.4_{oper_date}.csv', 'w', newline='') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(headers)
        writer.writerows(cursor)

except (Exception, Error) as error:
    print(f'Ошибка при работе с Postgres - {error}')
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение с Postgres закрыто')