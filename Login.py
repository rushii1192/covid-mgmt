from frontend.esha import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from form import LoginForm
import sys

class Login(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        print('I am login imported from Login')
        self.setupUi(self)
        self.changeWindow.clicked.connect(self.changeFrame)

    def changeFrame(self):
        print('hello world')
        self.hide()
        self.lf = LoginForm()
        self.lf.show()

app = QtWidgets.QApplication(sys.argv)

ui = Login()
#     ui.setupUi(LoginWindow)
ui.show()
sys.exit(app.exec_())

        # ui.setupUi(Dialog)
 
