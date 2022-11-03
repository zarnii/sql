import pymysql
conn = pymysql.connect(host='5.183.188.132',
                       user='db_vgu_student',
                       password='thasrCt3pKYWAYcK',
                       db='db_vgu_test',
                       charset='utf8'
                       )
print('подключение прошло')
cur = conn.cursor()
cur.execute(' SELECT table_name FROM information_schema.tables;')
data = cur.fetchall()
for row in data:
    print(row)

table = input('Из какой таблицы вывести данные: ')
cur.execute(f'SELECT * FROM {table};')
data = cur.fetchall()
for row in data:
    print(row)

conn.commit()
