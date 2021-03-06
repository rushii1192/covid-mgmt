# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\frontend\doctordashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_doctorDashboard(object):
    def setupUi(self, doctorDashboard):
        doctorDashboard.setObjectName("doctorDashboard")
        doctorDashboard.resize(1259, 684)
        doctorDashboard.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.appointments = QtWidgets.QWidget()
        self.appointments.setObjectName("appointments")
        self.patientName = QtWidgets.QLabel(self.appointments)
        self.patientName.setGeometry(QtCore.QRect(90, 50, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.patientName.setFont(font)
        self.patientName.setStyleSheet("background-color:rgb(199,230,255);\n"
"border-radius:12px;")
        self.patientName.setObjectName("patientName")
        self.problem = QtWidgets.QLabel(self.appointments)
        self.problem.setGeometry(QtCore.QRect(90, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.problem.setFont(font)
        self.problem.setStyleSheet("background-color:rgb(199,230,255);\n"
"border-radius:12px;")
        self.problem.setObjectName("problem")
        self.pastHistory = QtWidgets.QLabel(self.appointments)
        self.pastHistory.setGeometry(QtCore.QRect(90, 170, 181, 31))
        self.pastHistory.setStyleSheet("background-color:rgb(199,230,255);\n"
"border-radius:12px;")
        self.pastHistory.setObjectName("pastHistory")
        self.pastHistory_2 = QtWidgets.QLabel(self.appointments)
        self.pastHistory_2.setGeometry(QtCore.QRect(90, 240, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pastHistory_2.setFont(font)
        self.pastHistory_2.setStyleSheet("background-color:rgb(199,230,255);\n"
"border-radius:12px;")
        self.pastHistory_2.setObjectName("pastHistory_2")
        self.meetStart = QtWidgets.QPushButton(self.appointments)
        self.meetStart.setGeometry(QtCore.QRect(620, 140, 161, 51))
        self.meetStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.meetStart.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius:25px;\n"
"font: 16pt \"Segoe UI\";")
        self.meetStart.setObjectName("meetStart")
        self.prescribeMedicinesButton = QtWidgets.QPushButton(self.appointments)
        self.prescribeMedicinesButton.setGeometry(QtCore.QRect(320, 570, 291, 51))
        self.prescribeMedicinesButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prescribeMedicinesButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius:25px;\n"
"font: 16pt \"Segoe UI\";")
        self.prescribeMedicinesButton.setObjectName("prescribeMedicinesButton")
        self.widget = QtWidgets.QWidget(self.appointments)
        self.widget.setGeometry(QtCore.QRect(50, 20, 961, 621))
        self.widget.setStyleSheet("background-color:rgb(199,230,255);\n"
"border-radius:12px;")
        self.widget.setObjectName("widget")
        self.medicines = QtWidgets.QTextEdit(self.widget)
        self.medicines.setGeometry(QtCore.QRect(50, 300, 811, 221))
        self.medicines.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-radius:25px;\n"
"padding-left:10px;\n"
"padding-left:25px;")
        self.medicines.setObjectName("medicines")
        self.widget.raise_()
        self.patientName.raise_()
        self.problem.raise_()
        self.pastHistory.raise_()
        self.pastHistory_2.raise_()
        self.meetStart.raise_()
        self.prescribeMedicinesButton.raise_()
        doctorDashboard.addTab(self.appointments, "")
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.education = QtWidgets.QLineEdit(self.profile)
        self.education.setGeometry(QtCore.QRect(560, 350, 161, 41))
        self.education.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.education.setObjectName("education")
        self.label_4 = QtWidgets.QLabel(self.profile)
        self.label_4.setGeometry(QtCore.QRect(500, 130, 51, 51))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(".\\frontend\\images/add_phone_45px.png"))
        self.label_4.setObjectName("label_4")
        self.specialization = QtWidgets.QLineEdit(self.profile)
        self.specialization.setGeometry(QtCore.QRect(740, 350, 181, 41))
        self.specialization.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.specialization.setObjectName("specialization")
        self.label_5 = QtWidgets.QLabel(self.profile)
        self.label_5.setGeometry(QtCore.QRect(500, 270, 51, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(".\\frontend\\images/password_45px.png"))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.profile)
        self.label_7.setGeometry(QtCore.QRect(500, 440, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(".\\frontend\\images/address_45px.png"))
        self.label_7.setObjectName("label_7")
        self.changeButton = QtWidgets.QPushButton(self.profile)
        self.changeButton.setGeometry(QtCore.QRect(1010, 290, 191, 51))
        self.changeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"font: 16pt \"Segoe UI\";")
        self.changeButton.setObjectName("changeButton")
        self.label_9 = QtWidgets.QLabel(self.profile)
        self.label_9.setGeometry(QtCore.QRect(500, 340, 51, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(".\\frontend\\images/school_45px.png"))
        self.label_9.setObjectName("label_9")
        self.firstname = QtWidgets.QLineEdit(self.profile)
        self.firstname.setGeometry(QtCore.QRect(560, 70, 171, 41))
        self.firstname.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.firstname.setObjectName("firstname")
        self.password = QtWidgets.QLineEdit(self.profile)
        self.password.setGeometry(QtCore.QRect(560, 280, 271, 41))
        self.password.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(self.profile)
        self.label_3.setGeometry(QtCore.QRect(500, 200, 51, 51))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\frontend\\images/gmail_logo_45px.png"))
        self.label_3.setObjectName("label_3")
        self.lastName = QtWidgets.QLineEdit(self.profile)
        self.lastName.setGeometry(QtCore.QRect(760, 70, 171, 41))
        self.lastName.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.lastName.setObjectName("lastName")
        self.label_2 = QtWidgets.QLabel(self.profile)
        self.label_2.setGeometry(QtCore.QRect(500, 60, 51, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\frontend\\images/user_45px.png"))
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(self.profile)
        self.email.setGeometry(QtCore.QRect(560, 210, 371, 41))
        self.email.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.email.setObjectName("email")
        self.address = QtWidgets.QLineEdit(self.profile)
        self.address.setGeometry(QtCore.QRect(560, 420, 391, 81))
        self.address.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 25px;")
        self.address.setObjectName("address")
        self.mobile = QtWidgets.QLineEdit(self.profile)
        self.mobile.setGeometry(QtCore.QRect(560, 140, 261, 41))
        self.mobile.setStyleSheet("background-color: rgb(216, 216, 216);\n"
"border-radius: 20px;\n"
"padding-left:10px;")
        self.mobile.setObjectName("mobile")
        self.applyButton = QtWidgets.QPushButton(self.profile)
        self.applyButton.setGeometry(QtCore.QRect(1010, 360, 161, 51))
        self.applyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"font: 16pt \"Segoe UI\";")
        self.applyButton.setObjectName("applyButton")
        self.logoutButton = QtWidgets.QPushButton(self.profile)
        self.logoutButton.setGeometry(QtCore.QRect(1010, 220, 161, 51))
        self.logoutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.logoutButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"font: 16pt \"Segoe UI\";")
        self.logoutButton.setObjectName("logoutButton")
        self.label = QtWidgets.QLabel(self.profile)
        self.label.setGeometry(QtCore.QRect(0, 30, 461, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\frontend\\images/real-doctor.jpg"))
        self.label.setObjectName("label")
        doctorDashboard.addTab(self.profile, "")
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        self.historyFrame = QtWidgets.QFrame(self.history)
        self.historyFrame.setGeometry(QtCore.QRect(10, 20, 1201, 51))
        self.historyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.historyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.historyFrame.setObjectName("historyFrame")
        self.historyPatientName = QtWidgets.QLabel(self.historyFrame)
        self.historyPatientName.setGeometry(QtCore.QRect(30, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.historyPatientName.setFont(font)
        self.historyPatientName.setObjectName("historyPatientName")
        self.historyPatientProblem = QtWidgets.QLabel(self.historyFrame)
        self.historyPatientProblem.setGeometry(QtCore.QRect(270, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.historyPatientProblem.setFont(font)
        self.historyPatientProblem.setObjectName("historyPatientProblem")
        self.historyPatientAppoint = QtWidgets.QLabel(self.historyFrame)
        self.historyPatientAppoint.setGeometry(QtCore.QRect(740, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.historyPatientAppoint.setFont(font)
        self.historyPatientAppoint.setObjectName("historyPatientAppoint")
        self.historyPatientStatus = QtWidgets.QLabel(self.historyFrame)
        self.historyPatientStatus.setGeometry(QtCore.QRect(1000, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.historyPatientStatus.setFont(font)
        self.historyPatientStatus.setObjectName("historyPatientStatus")
        self.historyTable = QtWidgets.QTableWidget(self.history)
        self.historyTable.setGeometry(QtCore.QRect(10, 100, 1201, 491))
        self.historyTable.setObjectName("historyTable")
        self.historyTable.setColumnCount(0)
        self.historyTable.setRowCount(0)
        doctorDashboard.addTab(self.history, "")

        self.retranslateUi(doctorDashboard)
        doctorDashboard.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(doctorDashboard)

    def retranslateUi(self, doctorDashboard):
        _translate = QtCore.QCoreApplication.translate
        doctorDashboard.setWindowTitle(_translate("doctorDashboard", "Doctor Dashboard"))
        self.patientName.setText(_translate("doctorDashboard", "Patient Name"))
        self.problem.setText(_translate("doctorDashboard", "Patient Problem"))
        self.pastHistory.setText(_translate("doctorDashboard", "Patient Past History"))
        self.pastHistory_2.setText(_translate("doctorDashboard", "Prescribe Medicines"))
        self.meetStart.setText(_translate("doctorDashboard", "Create Meet"))
        self.prescribeMedicinesButton.setText(_translate("doctorDashboard", "Prescribe Medicines"))
        doctorDashboard.setTabText(doctorDashboard.indexOf(self.appointments), _translate("doctorDashboard", "Appointments"))
        self.education.setPlaceholderText(_translate("doctorDashboard", "Education"))
        self.specialization.setPlaceholderText(_translate("doctorDashboard", "Specialization"))
        self.changeButton.setText(_translate("doctorDashboard", "Change Details"))
        self.firstname.setPlaceholderText(_translate("doctorDashboard", "Enter Your First Name"))
        self.password.setPlaceholderText(_translate("doctorDashboard", "Enter your password"))
        self.lastName.setPlaceholderText(_translate("doctorDashboard", "Enter Your Last Name"))
        self.email.setPlaceholderText(_translate("doctorDashboard", "Enter Your mail"))
        self.address.setPlaceholderText(_translate("doctorDashboard", "Enter Your Address"))
        self.mobile.setPlaceholderText(_translate("doctorDashboard", "Enter Your mobile"))
        self.applyButton.setText(_translate("doctorDashboard", "Apply"))
        self.logoutButton.setText(_translate("doctorDashboard", "Log Out"))
        doctorDashboard.setTabText(doctorDashboard.indexOf(self.profile), _translate("doctorDashboard", "Profile"))
        self.historyPatientName.setText(_translate("doctorDashboard", "Patient Name"))
        self.historyPatientProblem.setText(_translate("doctorDashboard", "Problem"))
        self.historyPatientAppoint.setText(_translate("doctorDashboard", "Appointment Date"))
        self.historyPatientStatus.setText(_translate("doctorDashboard", "Status"))
        doctorDashboard.setTabText(doctorDashboard.indexOf(self.history), _translate("doctorDashboard", "History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    doctorDashboard = QtWidgets.QTabWidget()
    ui = Ui_doctorDashboard()
    ui.setupUi(doctorDashboard)
    doctorDashboard.show()
    sys.exit(app.exec_())
