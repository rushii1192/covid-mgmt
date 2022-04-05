import mysql.connector as mysql

#class for data connectivity with MySql
class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='db4free.net',
            database='covid_mgmt',
            user='sql6468008',
            password='eqHRn7SbqA'
        )
        # print("connected")
        # print(type(conn))
        return conn

dc = DatabaseConnection()
cursor = dc.cursor()
cursor.execute(f'SELECT * FROM appointment;')
result = cursor.fetchall()
for row in result:
    print(f'{row}\n type={type(row)}')