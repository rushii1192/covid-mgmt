from frontend.custRegisterWindow import Ui_RegisterWindow
from PyQt5 import QtWidgets
from backend import DatabaseConnection, EmailSender
from email.message import EmailMessage

class CustomerRegister(QtWidgets.QMainWindow,Ui_RegisterWindow):
    def __init__(self) -> None:
        super().__init__()
        print('I am Regsiter imported from Login')
        self.setupUi(self)
        # self.loginButton.clicked.connect(self.loginButtonAction)
        # self.changeWindow.clicked.connect(self.changeFrame)

    def register(self):
        fname = self.firstName.text()
        lname = self.lastName.text()
        email = self.email.text()
        mobile = self.mobile.text()
        psk = self.password.text()
        address = self.address.text()
        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute(f"INSERT INTO patient VALUES ('{fname}','{lname}',{mobile},'{email}','{address}','{psk}')")
        dc.commit()
        
        es = EmailSender()
        msg = EmailMessage()
        msg['subject'] = 'Query from customer'
        msg.set_content(f'Hi you are welcomed to our system.')
        es.sendEmail(email,str(msg))

        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Successfull')
        msg.setText(f'You have succesfully registered.\n{email} is your username.')
        msg.setStyleSheet('color:white')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        
    
    
