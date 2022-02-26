from Login import Login
from form import LoginForm
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

login = Login()
lf = LoginForm()

def loginButtonAction():
    usr = login.usrname.text()
    psk = login.password.text()
    if (usr=='Rushi' and psk=='Rushi123'):
        login.hide()
        lf.show()
    else:
        login.loginError()
    

login.loginButton.clicked.connect(loginButtonAction)
login.show()


sys.exit(app.exec_())
