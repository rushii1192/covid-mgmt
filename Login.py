from frontend.LoginWindow import Ui_LoginWindow
from PyQt5 import QtWidgets
from backend import DatabaseConnection

class Login(QtWidgets.QMainWindow,Ui_LoginWindow):
    __login = False
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

    def login(self):
        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute(f"SELECT * FROM patient WHERE Email = '{self.usrname.text()}' and Password = '{self.password.text()}'")
        if cursor.fetchone():
            return 1
        else:
            cursor.execute(f"SELECT * FROM doctor WHERE Email = '{self.usrname.text()}' and Password = '{self.password.text()}'")
            if cursor.fetchone():
                return 2
            return 0

    def setLogin(self):
        self.__login = True
