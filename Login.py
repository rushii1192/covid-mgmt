from frontend.LoginWindow import Ui_LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from form import LoginForm
import sys

class Login(QtWidgets.QMainWindow,Ui_LoginWindow):
    def __init__(self) -> None:
        super().__init__()
        print('I am login imported from Login')
        self.setupUi(self)
        # self.loginButton.clicked.connect(self.loginButtonAction)
        # self.changeWindow.clicked.connect(self.changeFrame)

    def loginError(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Login Error')
        msg.setText('Hey You have entered wrong credintials\nPlease check your username and password')
        msg.setStyleSheet('color:white')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        # ui.setupUi(Dialog)
 
