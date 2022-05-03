from frontend.custRegisterWindow import Ui_RegisterWindow
from frontend.doctorRegisterWindow import Ui_DoctorRegisterWindow
from PyQt5 import QtWidgets, QtGui
from backend import DatabaseConnection, EmailSender, Validator
from email.message import EmailMessage

class CustomerRegister(QtWidgets.QMainWindow,Ui_RegisterWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))   
        # self.loginButton.clicked.connect(self.loginButtonAction)
        # self.changeWindow.clicked.connect(self.changeFrame)

    def register(self):
        valid = Validator()
        fname = self.firstName.text()
        lname = self.lastName.text()
        email = self.email.text()
        mobile = self.mobile.text()
        psk = self.password.text()
        address = self.address.text()
        print(psk)
        print(self.cnfrmPassword.text())        
        if valid.checkNullValues(fname) and valid.checkNullValues(lname) and valid.checkNullValues(email) and valid.checkNullValues(mobile) and valid.checkNullValues(psk) and valid.checkNullValues(address):
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle('UnSuccessfull')
            msg.setText(f'Any of required field is black')
            msg.setStyleSheet('color:black')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False

        elif psk is self.cnfrmPassword.text():
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle('UnSuccessfull')
            msg.setText(f'Password and cnfrm password does not match.')
            msg.setStyleSheet('color:black')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False

        elif not valid.passwordValidator(psk)[0]:
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle('UnSuccessfull')
            msg.setText(f'Password is not enough strong\n{valid.passwordValidator(psk)[1]}')
            msg.setStyleSheet('color:black')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return False

        else:
            try:
                dc = DatabaseConnection()
                cursor = dc.cursor()
                cursor.execute(f"INSERT INTO patient VALUES ('{fname}','{lname}',{mobile},'{email}','{address}','{psk}')")
                dc.commit()
                es = EmailSender()
                msg = EmailMessage()
                msg['subject'] = 'Registered Succefully to system'
                msg.set_content(f'You have sucessfully regusterd for the sytem with username-{self.email.text()} and password-{self.password.text()}.')
                es.sendEmail(email,str(msg))

                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle('Successfull')
                msg.setText(f'You have succesfully registered.\n{email} is your username.')
                msg.setStyleSheet('color:black')
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                return True

            except:
                msg = QtWidgets.QMessageBox(self)
                msg.setWindowTitle('UnSuccessfull')
                msg.setText(f'Some error has ocuured please try again.Please check your mobile and email')
                msg.setStyleSheet('color:black')
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
                return False
class DoctorRegister(QtWidgets.QMainWindow,Ui_DoctorRegisterWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))   

    def register(self):
        fname = self.firstname.text()
        lname = self.lastName.text()
        mobile = self.mobile.text()
        email = self.email.text()
        address = self.address.text()
        psk = self.password.text()
        edu = self.education.text()
        spec = self.specialization.text()

        if self.password.text()==self.cnfrmPassword.text():
            msg = QtWidgets.QMessageBox(self)
            msg.setWindowTitle('Successfull')
            msg.setText(f'Password and cnfrm password does not match.')
            msg.setStyleSheet('color:black')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute(f"INSERT INTO doctor VALUES ('{fname}','{lname}',{mobile},'{email}','{address}','{psk}','{edu}','{spec}');")
        dc.commit()

        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Successfull')
        msg.setText(f'You have succesfully registered.\n{email} is your username.')
        msg.setStyleSheet('color:black')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    
