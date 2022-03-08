#Database Connection
import mysql.connector as mysql
import smtplib

#class for data connectivity with MySql
class DatabaseConnection(object):
    def __new__(cls, *args, **kwargs):
        conn = mysql.connect(
            host='db4free.net',
            database='covid_mgmt',
            user='sql6468008',
            password='eqHRn7SbqA'
        )
        print("connected")
        print(type(conn))
        return conn

    def __del__(self):
        self.conn.close()

#Exception Handling
dc = DatabaseConnection()