from Login import Login
from register import CustomerRegister, DoctorRegister
from dashboard import CustomerDashboard, DoctorDashboard
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

login = Login()

custRegister = CustomerRegister()
custdash = CustomerDashboard()

docRegister = DoctorRegister()
docdash = DoctorDashboard()

# when login button on login page is clicked
def loginButtonAction():
    if login.login() == 1:
        login.hide()
        custdash.show()
    elif login.login() == 2:
        login.hide()
        docdash.show()
    else:
        login.loginError()
    
# when register button on login is clicked
def registerButtonAction():
    login.hide()
    custRegister.show()

# when register button on custregister page is clicked
def custRegisterButtonAction():
    custRegister.register()
    custRegister.hide()
    login.show()

# when register as dcotor button on custregister page is clicked
def custDoctorRegisterButtonAction():
    custRegister.hide()
    docRegister.show()

# when register as dcotor button on custregister page is clicked
def docDoctorRegisterButtonAction():
    docRegister.register()
    docRegister.hide()
    login.show()

login.loginButton.clicked.connect(loginButtonAction)
login.registerButton.clicked.connect(registerButtonAction)

custRegister.registerButton.clicked.connect(custRegisterButtonAction)
custRegister.doctorRegisterButton.clicked.connect(custDoctorRegisterButtonAction)

docRegister.registerButton.clicked.connect(docDoctorRegisterButtonAction)

login.show()


sys.exit(app.exec_())
