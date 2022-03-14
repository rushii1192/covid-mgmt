# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/doctordashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DoctorDashboard(object):
    def setupUi(self, DoctorDashboard):
        DoctorDashboard.setObjectName("DoctorDashboard")
        DoctorDashboard.resize(854, 750)
        DoctorDashboard.setStyleSheet("background-color:rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(DoctorDashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 301, 691))
        self.widget.setStyleSheet("background-color:rgb(1,76,120);\n"
"color:rgb(255,255,255);\n"
"border-radius:8px;\n"
"padding-left:10px;\n"
"border:2px solid rgb(1,76,120);\n"
"border-bottom-color:rgb(0, 0, 102);")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 120, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgb(1,76,120);\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"border:2px solid rgb(1,76,120);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 180, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgb(1,76,120);\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"border:2px solid rgb(1,76,120);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 250, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgb(1,76,120);\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"border:2px solid rgb(1,76,120);\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 310, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgb(1,76,120);\n"
"color:rgb(255,255,255);\n"
"padding-left:10px;\n"
"border:2px solid rgb(1,76,120);\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 100, 61, 51))
        self.label.setStyleSheet("border-bottom-color:rgb(1, 76, 120);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("frontend\\images/user_secured_45px.png"))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.label_5.setStyleSheet("border-bottom-color:rgb(1, 76, 120);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("frontend\\images/schedule_45px.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 61, 51))
        self.label_6.setStyleSheet("border-bottom-color:rgb(1, 76, 120);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("frontend\\images/ecg_45px.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 300, 61, 51))
        self.label_7.setStyleSheet("border-bottom-color:rgb(1, 76, 120);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("frontend\\images/Logout_45px.png"))
        self.label_7.setObjectName("label_7")
        DoctorDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DoctorDashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        DoctorDashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DoctorDashboard)
        self.statusbar.setObjectName("statusbar")
        DoctorDashboard.setStatusBar(self.statusbar)

        self.retranslateUi(DoctorDashboard)
        QtCore.QMetaObject.connectSlotsByName(DoctorDashboard)

    def retranslateUi(self, DoctorDashboard):
        _translate = QtCore.QCoreApplication.translate
        DoctorDashboard.setWindowTitle(_translate("DoctorDashboard", "MainWindow"))
        self.lineEdit.setText(_translate("DoctorDashboard", "Profile Details"))
        self.lineEdit_2.setText(_translate("DoctorDashboard", "Appointments"))
        self.lineEdit_3.setText(_translate("DoctorDashboard", "My Patients"))
        self.lineEdit_4.setText(_translate("DoctorDashboard", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DoctorDashboard = QtWidgets.QMainWindow()
    ui = Ui_DoctorDashboard()
    ui.setupUi(DoctorDashboard)
    DoctorDashboard.show()
    sys.exit(app.exec_())
