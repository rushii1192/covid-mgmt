from frontend.LoginWindow import Ui_LoginWindow
from PyQt5 import QtWidgets, QtGui
from backend import DatabaseConnection

class Login(QtWidgets.QMainWindow,Ui_LoginWindow):
    __login = False
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))   
        # self.loginButton.clicked.connect(self.loginButtonAction)
        # self.changeWindow.clicked.connect(self.changeFrame)

    def loginError(self):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Login Error')
        msg.setText('Hey You have entered wrong credintials\nPlease check your username and password')
        msg.setStyleSheet('color:black')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        # ui.setupUi(Dialog)

    def login(self):
        dc = DatabaseConnection()
        cursor = dc.cursor()
        cursor.execute(f"SELECT * FROM patient WHERE Email = '{self.usrname.text()}' and Password = '{self.password.text()}'")
        result = cursor.fetchone()
        if result:
            return (1,result[3])
        else:
            cursor.execute(f"SELECT * FROM doctor WHERE Email = '{self.usrname.text()}' and Password = '{self.password.text()}'")
            result = cursor.fetchone()
            if result:
                return (2,result[3])
            return (0,"error")

    def setLogin(self):
        self.__login = True
