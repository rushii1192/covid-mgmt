from PyQt5 import QtWidgets
from frontend.custDashboardWindow import Ui_CustomerDashboardWindow
from frontend.doctorDashboardWindow import Ui_DoctorDashboard
from frontend.maindashboard import Ui_MainDashboard

class CustomerDashboard(QtWidgets.QMainWindow,Ui_CustomerDashboardWindow):
    def __init__(self) -> None:
        super().__init__()
        print('I am Regsiter imported from Login')
        self.setupUi(self)

class DoctorDashboard(QtWidgets.QMainWindow,Ui_DoctorDashboard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

class WelcomePage(QtWidgets.QMainWindow,Ui_MainDashboard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logoutButton.hide()
