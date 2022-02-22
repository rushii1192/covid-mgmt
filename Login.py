from frontend.LoginWindow import Ui_LoginWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from form import LoginForm
import sys

class Login(QtWidgets.QMainWindow,Ui_LoginWindow):
    def __init__(self) -> None:
        super().__init__()
        print('I am login imported from Login')
        self.setupUi(self)
        self.loginButton.clicked.connect(self.changeFrame)
        # self.changeWindow.clicked.connect(self.changeFrame)

    def changeFrame(self):
        print('hello world')
        

        # ui.setupUi(Dialog)
 
