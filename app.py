from Login import Login
from register import CustomerRegister
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

login = Login()
custRegister = CustomerRegister()

def loginButtonAction():
    usr = login.usrname.text()
    psk = login.password.text()
    if (usr=='Rushi' and psk=='Rushi123'):
        login.hide()
    else:
        login.loginError()
    
def registerButtonAction():
    login.hide()
    custRegister.show()

login.loginButton.clicked.connect(loginButtonAction)
login.registerButton.clicked.connect(registerButtonAction)
login.show()


sys.exit(app.exec_())
