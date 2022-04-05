# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\frontend\maindashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainDashboard(object):
    def setupUi(self, MainDashboard):
        MainDashboard.setObjectName("MainDashboard")
        MainDashboard.resize(1272, 744)
        MainDashboard.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(MainDashboard)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 241, 691))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 241, 821))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 161, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\frontend\\images/medical-logo.jpg"))
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.widget)
        self.loginButton.setGeometry(QtCore.QRect(10, 270, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginButton.setFont(font)
        self.loginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginButton.setAutoFillBackground(False)
        self.loginButton.setStyleSheet("QPushButton#loginButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#loginButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(self.widget)
        self.registerButton.setGeometry(QtCore.QRect(10, 310, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.registerButton.setFont(font)
        self.registerButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerButton.setStyleSheet("QPushButton#registerButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#registerButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.registerButton.setObjectName("registerButton")
        self.dashboardButton = QtWidgets.QPushButton(self.widget)
        self.dashboardButton.setGeometry(QtCore.QRect(10, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dashboardButton.setFont(font)
        self.dashboardButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dashboardButton.setStyleSheet("QPushButton#dashboardButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#dashboardButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.dashboardButton.setObjectName("dashboardButton")
        self.doctorButton = QtWidgets.QPushButton(self.widget)
        self.doctorButton.setGeometry(QtCore.QRect(10, 350, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doctorButton.setFont(font)
        self.doctorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.doctorButton.setStyleSheet("QPushButton#doctorButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#doctorButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.doctorButton.setObjectName("doctorButton")
        self.historyButton = QtWidgets.QPushButton(self.widget)
        self.historyButton.setGeometry(QtCore.QRect(10, 390, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.historyButton.setFont(font)
        self.historyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.historyButton.setStyleSheet("QPushButton#historyButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#historyButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.historyButton.setObjectName("historyButton")
        self.logoutButton = QtWidgets.QPushButton(self.widget)
        self.logoutButton.setGeometry(QtCore.QRect(10, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.logoutButton.setFont(font)
        self.logoutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet("QPushButton#logoutButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-radius:15px;\n"
"    color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#logoutButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}")
        self.logoutButton.setObjectName("logoutButton")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(0, 670, 241, 80))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_4.setObjectName("widget_4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(270, 80, 120, 80))
        self.widget_2.setObjectName("widget_2")
        self.statusbar = QtWidgets.QStatusBar(MainDashboard)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 25))
        self.statusbar.setObjectName("statusbar")
        self.doctorSearchText = QtWidgets.QLineEdit(MainDashboard)
        self.doctorSearchText.setGeometry(QtCore.QRect(280, 240, 351, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doctorSearchText.setFont(font)
        self.doctorSearchText.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:20px;\n"
"padding-left:10px;\n"
"padding-bottom:3px")
        self.doctorSearchText.setObjectName("doctorSearchText")
        self.doctorSearchButton = QtWidgets.QPushButton(MainDashboard)
        self.doctorSearchButton.setGeometry(QtCore.QRect(670, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doctorSearchButton.setFont(font)
        self.doctorSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.doctorSearchButton.setStyleSheet("QPushButton#doctorSearchButton{\n"
"    border-radius:20px;\n"
"    padding-left:5px;\n"
"    color:rgb(255, 255, 255);\n"
"    background-color:rgb(0, 0, 127);\n"
"}\n"
"")
        self.doctorSearchButton.setObjectName("doctorSearchButton")
        self.widget_3 = QtWidgets.QWidget(MainDashboard)
        self.widget_3.setGeometry(QtCore.QRect(270, 290, 931, 61))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(460, 20, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(600, 20, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(730, 20, 71, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainDashboard)
        self.label_6.setGeometry(QtCore.QRect(270, 20, 931, 201))
        self.label_6.setStyleSheet("padding-left:150px;\n"
"background-color: rgb(166, 197, 255);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(".\\frontend\\images/dashboard_img.jpg"))
        self.label_6.setObjectName("label_6")
        self.doctorsTable = QtWidgets.QTableWidget(MainDashboard)
        self.doctorsTable.setGeometry(QtCore.QRect(270, 370, 931, 351))
        self.doctorsTable.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.doctorsTable.setObjectName("doctorsTable")
        self.doctorsTable.setColumnCount(0)
        self.doctorsTable.setRowCount(0)

        self.retranslateUi(MainDashboard)
        QtCore.QMetaObject.connectSlotsByName(MainDashboard)

    def retranslateUi(self, MainDashboard):
        _translate = QtCore.QCoreApplication.translate
        MainDashboard.setWindowTitle(_translate("MainDashboard", "CustomerDashboard"))
        self.loginButton.setText(_translate("MainDashboard", "Login"))
        self.registerButton.setText(_translate("MainDashboard", "Register"))
        self.dashboardButton.setText(_translate("MainDashboard", "Dashboard"))
        self.doctorButton.setText(_translate("MainDashboard", "Doctor"))
        self.historyButton.setText(_translate("MainDashboard", "History"))
        self.logoutButton.setText(_translate("MainDashboard", "LogOut"))
        self.doctorSearchText.setPlaceholderText(_translate("MainDashboard", "Search Doctors"))
        self.doctorSearchButton.setText(_translate("MainDashboard", "Search"))
        self.label_2.setText(_translate("MainDashboard", "Name"))
        self.label_3.setText(_translate("MainDashboard", "Degree"))
        self.label_4.setText(_translate("MainDashboard", "Speciality"))
        self.label_5.setText(_translate("MainDashboard", "Ratings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainDashboard = QtWidgets.QWidget()
    ui = Ui_MainDashboard()
    ui.setupUi(MainDashboard)
    MainDashboard.show()
    sys.exit(app.exec_())
