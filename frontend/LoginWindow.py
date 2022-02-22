# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(656, 590)
        LoginWindow.setStyleSheet("background-color:rgba(16,16,16,255);\n"
"border radius:20px;")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usrname = QtWidgets.QLineEdit(self.centralwidget)
        self.usrname.setGeometry(QtCore.QRect(80, 250, 501, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usrname.setFont(font)
        self.usrname.setStyleSheet("background-color:rgba(47,49,52,200);\n"
"color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"border:1px solid rgba(0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"padding-bottom:3px")
        self.usrname.setObjectName("usrname")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 310, 501, 40))
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
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(250, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color:rgb(255,191,16);\n"
"color:rgb(135,60,0);\n"
"border-radius:20px;\n"
"\n"
"Qpushbutton#b1:pressed{\n"
"background-color:rgb(255,255,16);\n"
"}\n"
"\n"
"")
        self.loginButton.setObjectName("loginButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 80, 421, 121))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,191,16);")
        self.label.setObjectName("label")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 26))
        self.menubar.setObjectName("menubar")
        self.menulogin = QtWidgets.QMenu(self.menubar)
        self.menulogin.setObjectName("menulogin")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menulogin.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.usrname.setPlaceholderText(_translate("LoginWindow", "Enter the username"))
        self.password.setPlaceholderText(_translate("LoginWindow", "Enter the password"))
        self.loginButton.setText(_translate("LoginWindow", "L o g i n"))
        self.label.setText(_translate("LoginWindow", ""))
        self.menulogin.setTitle(_translate("LoginWindow", "login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
