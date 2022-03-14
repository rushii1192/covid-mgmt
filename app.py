from Login import Login
from register import CustomerRegister
from PyQt5 import QtWidgets
from form import LoginForm
import sys


app = QtWidgets.QApplication(sys.argv)

login = Login()
custRegister = CustomerRegister()
lf = LoginForm()

def loginButtonAction():
    if login.login():
        login.hide()
        lf.show()
    else:
        login.loginError()
    
def registerButtonAction():
    login.hide()
    custRegister.show()

def custRegisterButtonAction():
    custRegister.register()
    custRegister.hide()
    login.show()

login.loginButton.clicked.connect(loginButtonAction)
login.registerButton.clicked.connect(registerButtonAction)
custRegister.registerButton.clicked.connect(custRegisterButtonAction)
login.show()


sys.exit(app.exec_())
