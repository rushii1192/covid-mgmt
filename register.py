from frontend.custRegisterWindow import Ui_RegisterWindow
from PyQt5 import QtWidgets

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
        print(f'{fname},{lname},{email},{mobile},{psk},{address}')
    
    
