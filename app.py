from Login import Login
from form import LoginForm
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

ui = Login()
lf = LoginForm()

def changeLabel():
    # ui.changeWindow.clicked.connect(changeFrame)
    ui.show()
    lf.hide()

def changeFrame():
    print('You have clicked change form')
    lf.addButton.clicked.connect(changeLabel)
    lf.show()
    ui.hide()

ui.changeWindow.clicked.connect(changeFrame)
ui.show()


sys.exit(app.exec_())
