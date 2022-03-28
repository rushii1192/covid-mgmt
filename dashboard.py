from PyQt5 import QtWidgets, QtGui
from frontend.custDashboardWindow import Ui_CustomerDashboardWindow
from frontend.doctorDashboardWindow import Ui_DoctorDashboard
from frontend.maindashboard import Ui_MainDashboard
from frontend.doctorProfileWidget import Ui_DoctorProfile

class CustomerDashboard(QtWidgets.QMainWindow,Ui_CustomerDashboardWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))   

class DoctorDashboard(QtWidgets.QMainWindow,Ui_DoctorDashboard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.profileButton.clicked.connect(self.profileButtonAction)
        profile_ui = Ui_DoctorProfile()
        profile_ui.setupUi(self.mainContainer)
        self.mainContainer.show()    
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))    
    
    def profileButtonAction(self):
        print('This is clickefd')
        
class WelcomePage(QtWidgets.QMainWindow,Ui_MainDashboard):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logoutButton.hide()
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))   
