from PyQt5 import QtWidgets, QtGui,QtCore
from frontend.custDashboardWindow import Ui_CustomerDashboardWindow
from frontend.doctorDashboardWindow import Ui_doctorDashboard
from frontend.maindashboard import Ui_MainDashboard
from frontend.doctorProfileWidget import Ui_DoctorProfile
from frontend.individualHistory import Ui_IndividualHistory
from backend import DatabaseConnection, MeetCreator
from patientOptions import PatientHistory, PatientAppointment
import webbrowser as wb
import time
import pyautogui as pyg

class DoctorDashboard(QtWidgets.QTabWidget,Ui_doctorDashboard):
    __dc = DatabaseConnection()
    __cursor = __dc.cursor()
    __doctorId = ""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        # self.profileButton.clicked.connect(self.profileButtonAction)
        self.setWindowIcon(QtGui.QIcon('frontend/images/medical-logo.jpg'))
        self.applyButton.hide()
        self.setEditState(True)
        self.changeButton.clicked.connect(lambda:self.setEditState(False))
        self.meetStart.clicked.connect(self.createMeet)

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
        meet_url = meet.createMeeting('2022-04-04T07: 04: 25')
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome"
        wb.open(meet_url, new=2)  # open zoom link in a new window
        # time.sleep(5)  # given time for the link to show app top-up window
        # pyg.click(x=805, y=254, clicks=1, interval=0, button='left')  # click on open zoom.app option
        # time.sleep(10)  # wait for 10 sec
        # pyg.click(x=195, y=31, clicks=1, interval=0, button='left')  # maximize zoom app
        # time.sleep(3)  # wait for 3 sec
        # pyg.click(x=50, y=776, clicks=1, interval=0, button='left')

    def logout(self):
        self.__dc.close()

    def showHistory(self):
        self.__cursor.execute(f"SELECT * FROM appointment WHERE DoctorId = '{self.__doctorId}';")
        print('query is executed')
        result = self.__cursor.fetchall()
        for row in result:
            print(row)
            ui = Ui_IndividualHistory()
            ui.setupUi(self.historyArea)
            ui.historyPatientName.setText("helo")
        self.historyArea.show()

    def setDoctorId(self,docId):
        self.__doctorId = docId

class WelcomePage(QtWidgets.QMainWindow,Ui_MainDashboard):
    __customerId = ""
    __dc = DatabaseConnection()
    __cursor = __dc.cursor()
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

    def setCustomerId(self,custId):
        self.__customerId = custId   
        self.loginButton.setText(self.__customerId)

    def showHistory(self):
        self.ph = PatientHistory()
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

    def gotoAppointment(self):
        self.pa = PatientAppointment()
        self.pa.setIds("atharva@gmail.com",self.__customerId)
        for i in self.doctorsTable.selectionModel().selectedIndexes():
            print(i.row())
        self.pa.show()

