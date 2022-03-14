# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(665, 732)
        RegisterWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(80, 220, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.firstName.setFont(font)
        self.firstName.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(f,f,f,f);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom-3px\n"
"")
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(330, 220, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lastName.setFont(font)
        self.lastName.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(f,f,f,f);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom-3px\n"
"")
        self.lastName.setObjectName("lastName")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(80, 280, 481, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.email.setFont(font)
        self.email.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(f,f,f,f);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom-3px\n"
"")
        self.email.setObjectName("email")
        self.mobile = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(80, 340, 231, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mobile.setFont(font)
        self.mobile.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(f,f,f,f);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom-3px\n"
"")
        self.mobile.setObjectName("mobile")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 400, 311, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom:3px")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.cnfrmPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.cnfrmPassword.setGeometry(QtCore.QRect(80, 460, 311, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cnfrmPassword.setFont(font)
        self.cnfrmPassword.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom:3px")
        self.cnfrmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cnfrmPassword.setObjectName("cnfrmPassword")
        self.address = QtWidgets.QLineEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(80, 520, 521, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address.setFont(font)
        self.address.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(f,f,f,f);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom-3px\n"
"")
        self.address.setObjectName("address")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(240, 640, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.registerButton.setFont(font)
        self.registerButton.setStyleSheet("background-color:rgb(255,191,16);\n"
"color:rgb(135,60,0);\n"
"border-radius:20px;\n"
"\n"
"Qpushbutton#loginButton:pressed{\n"
"background-color:rgb(255,255,16);\n"
"}\n"
"\n"
"")
        self.registerButton.setObjectName("registerButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 151, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("frontend\\images/register.png"))
        self.label.setObjectName("label")
        RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "RegisterWindow"))
        self.firstName.setPlaceholderText(_translate("RegisterWindow", "Enter First Name"))
        self.lastName.setPlaceholderText(_translate("RegisterWindow", "Enter Last Name"))
        self.email.setPlaceholderText(_translate("RegisterWindow", "Enter Email"))
        self.mobile.setPlaceholderText(_translate("RegisterWindow", "Enter Mobile"))
        self.password.setPlaceholderText(_translate("RegisterWindow", "Enter the password"))
        self.cnfrmPassword.setPlaceholderText(_translate("RegisterWindow", "Confirm the password"))
        self.address.setPlaceholderText(_translate("RegisterWindow", "Enter your address"))
        self.registerButton.setText(_translate("RegisterWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindow = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindow()
    ui.setupUi(RegisterWindow)
    RegisterWindow.show()
    sys.exit(app.exec_())