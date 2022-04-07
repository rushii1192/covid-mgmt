from PyQt5 import QtWidgets, QtGui,QtCore
from frontend.doctorDashboardWindow import Ui_doctorDashboard
from frontend.maindashboard import Ui_MainDashboard
from backend import DatabaseConnection, MeetCreator, EmailSender
from patientOptions import PatientHistory, PatientAppointment
import webbrowser as wb
from email.message import EmailMessage

class DoctorDashboard(QtWidgets.QTabWidget,Ui_doctorDashboard):
    __dc = DatabaseConnection()
    __cursor = __dc.cursor(buffered=True)
    __doctorId = ""
    meet_url = ""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # self.profileButton.clicked.connect(self.profileButtonAction)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))
        self.applyButton.hide()
        self.setEditState(True)
        self.changeButton.clicked.connect(lambda:self.setEditState(False))
        self.meetStart.clicked.connect(self.createMeet)
        self.historyTable.setRowCount(20)
        self.historyTable.setColumnCount(3)
        self.historyTable.setColumnWidth(0, 250)
        self.historyTable.setColumnWidth(1, 250)
        self.historyTable.setColumnWidth(2, 250)
        self.historyTable.verticalHeader().hide()
        self.historyTable.horizontalHeader().hide()
        self.prescribeMedicinesButton.clicked.connect(self.prescribeMedicineButtonAction)
        self.applyButton.clicked.connect(self.updateProfile)

    def setEditState(self,value):
        self.firstname.setReadOnly(value)
        self.lastName.setReadOnly(value)
        self.mobile.setReadOnly(value)
        self.email.setReadOnly(value)
        self.password.setReadOnly(value)
        self.education.setReadOnly(value)
        self.specialization.setReadOnly(value)
        self.address.setReadOnly(value)
        if not(value):
            self.applyButton.show()
    
    def createMeet(self):
        meet = MeetCreator()
        self.meet_url = meet.createMeeting('2022-04-04T07: 04: 25')
        wb.open(self.meet_url, new=2)  # open zoom link in a new window
        es = EmailSender()
        msg = EmailMessage()
        msg['subject'] = 'Link for the meet'
        msg.set_content(f'''click on bellow link to meet your doctor
                    \n{self.meet_url}
                ''')
        es.sendEmail(self.patientName.text(), str(msg))

    def logout(self):
        pass

    def prescribeMedicineButtonAction(self):
        es = EmailSender()
        msg = EmailMessage()
        msg['subject'] = 'Your Prescription'
        msg.set_content(f'''The prescription is
            \n{self.medicines.toPlainText()}
        ''')
        es.sendEmail(self.patientName.text(), str(msg))
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Successfull')
        msg.setText(f'Prescription has been mailed to patient.')
        msg.setStyleSheet('color:black')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def updateProfile(self):
        self.__cursor.execute(f"UPDATE doctor SET FirstName='{self.firstname.text()}',LastName='{self.lastName.text()}',Mobile={self.mobile.text()},Email='{self.email.text()}',Address='{self.address.text()}',Password='{self.password.text()}',Education='{self.education.text()}',Specialization='{self.specialization.text()}' WHERE Email='{self.__doctorId}';")
        self.__dc.commit()
        self.__cursor = self.__dc.cursor(buffered=True)
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Successfull')
        msg.setText(f'Your profile details has been updated.\nlogout and login again to see changes.')
        msg.setStyleSheet('color:black')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def setDoctorId(self,docId):
        self.__doctorId = docId
        # for loading history of doctor
        self.__cursor.execute(f"SELECT * FROM appointment WHERE DoctorId = '{self.__doctorId}';")
        print('query is executed')
        result = self.__cursor.fetchall()
        for count, row in enumerate(result):
            self.historyTable.setItem(count, 0, QtWidgets.QTableWidgetItem(f'{row[-2]}'))
            self.historyTable.setItem(count, 1, QtWidgets.QTableWidgetItem(f'{row[-1]}'))
            self.historyTable.setItem(count, 2, QtWidgets.QTableWidgetItem(f'{row[1]}'))

        # for loding profile details
        self.__cursor.execute(f"SELECT * FROM doctor WHERE Email='{self.__doctorId}';")
        result = self.__cursor.fetchone()
        self.firstname.setText(result[0])
        self.lastName.setText(result[1])
        self.mobile.setText(f'{result[2]}')
        self.email.setText(result[3])
        self.address.setText(result[4])
        self.password.setText(result[5])
        self.education.setText(result[6])
        self.specialization.setText(result[7])

        # for loading current appointment
        self.__cursor.execute(f"SELECT * FROM appointment WHERE DoctorId='{self.__doctorId}'")
        result = self.__cursor.fetchone()
        self.patientName.setText(result[-2])
        self.pastHistory.setText("")
        self.problem.setText(result[-1])

class WelcomePage(QtWidgets.QMainWindow,Ui_MainDashboard):
    __customerId = ""
    __dc = DatabaseConnection()
    __cursor = __dc.cursor()
    __doctorsList = []
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logoutButton.hide()
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))
        self.historyButton.clicked.connect(self.showHistory)
        self.historyButton.hide()
        self.doctorsTable.horizontalHeader().hide()
        self.doctorsTable.verticalHeader().hide()
        self.doctorsTable.setColumnCount(4)
        self.doctorsTable.setRowCount(50)
        self.doctorsTable.setColumnWidth(0,450)
        self.doctorsTable.setColumnWidth(2,175)
        self.setDoctors()
        self.joinMeetButton.hide()


    def setCustomerId(self,custId,doctor):
        self.__customerId = custId   
        self.loginButton.setText(self.__customerId)
        self.joinMeetButton.clicked.connect(lambda :self.joinMeetButtonAction(doctor))

    def showHistory(self):
        self.ph = PatientHistory(self.__customerId)
        self.ph.show()

    def setDoctors(self):
        self.__cursor.execute(f'SELECT * FROM doctor;')
        result = self.__cursor.fetchall()
        for count,row in enumerate(result):
            gotoButton = QtWidgets.QPushButton()
            gotoButton.setText("Book Appointment")
            gotoButton.setStyleSheet("background-color:rgb(0,0,127);color:rgb(255,255,255)")
            gotoButton.clicked.connect(self.gotoAppointment)
            self.doctorsTable.setItem(count, 0,QtWidgets.QTableWidgetItem(f'{row[0]} {row[1]}'))
            self.doctorsTable.setItem(count, 1, QtWidgets.QTableWidgetItem(f'{row[-2]}'))
            self.doctorsTable.setItem(count, 2, QtWidgets.QTableWidgetItem(f'{row[-1]}'))
            self.doctorsTable.setCellWidget(count, 3, gotoButton)
            self.__doctorsList.append(row[3])

    def gotoAppointment(self):
        self.pa = PatientAppointment()

        for i in self.doctorsTable.selectionModel().selectedIndexes():
            self.pa.setIds(self.__doctorsList[i.row()], self.__customerId)
        self.pa.show()

    def joinMeetButtonAction(self,db):
        print(db.meet_url)
        wb.open(db.meet_url, new=2)


