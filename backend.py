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
        # print("connected")
        # print(type(conn))
        return conn

# email sender class
class EmailSender(object):
    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com")
        self.server.login("rushikeshborakhede@student.sfit.ac.in", "Rushi_1192#")

    def sendEmail(self,receiver,content):
        self.server.sendmail('rushikeshborakhede@student.sfit.ac.in',receiver,content)

        
    
#Exception Handling
