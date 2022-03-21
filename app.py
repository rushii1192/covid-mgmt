from tkinter import Button
from Login import Login
from register import CustomerRegister, DoctorRegister
from dashboard import CustomerDashboard, DoctorDashboard, WelcomePage
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

login = Login()
welcome = WelcomePage()

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

# when logout of doctor is clicked
def docDashLogoutButtonAction():
    docdash.hide()
    login.show()

# when login on welcome page is clicked
def loginWelcomePageAction():
    login.show()

# when register on welcome page is clicked
def registerWelcomePageAction():
    custRegister.show()

# actions of login page Button
login.loginButton.clicked.connect(loginButtonAction)
login.registerButton.clicked.connect(registerButtonAction)

# actions of cutomer register page Button
custRegister.registerButton.clicked.connect(custRegisterButtonAction)
custRegister.doctorRegisterButton.clicked.connect(custDoctorRegisterButtonAction)

# action of doctor register page Button
docRegister.registerButton.clicked.connect(docDoctorRegisterButtonAction)

# action of doctor dashboard Button
docdash.logoutButton.clicked.connect(docDashLogoutButtonAction)

# actions on welcome page buttons
welcome.loginButton.clicked.connect(loginWelcomePageAction)
welcome.registerButton.clicked.connect(registerWelcomePageAction)

welcome.show()

sys.exit(app.exec_())
