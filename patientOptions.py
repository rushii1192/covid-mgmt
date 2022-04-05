
from frontend.patientHistoryWindow import Ui_PatientHistory
from frontend.patientAppointmentWindow import Ui_PatientAppointment
from PyQt5 import QtWidgets,QtGui

class PatientHistory(QtWidgets.QMainWindow,Ui_PatientHistory):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        currentRow = self.historyTable.rowCount()
        self.historyTable.verticalHeader().setVisible(False)
        self.historyTable.horizontalHeader().setVisible(False)
        self.historyTable.setColumnCount(3)
        self.historyTable.setRowCount(10)
        self.historyTable.insertRow(currentRow)
        self.historyTable.setColumnWidth(0, 300)
        self.historyTable.setColumnWidth(1, 300)
        self.historyTable.setColumnWidth(2, 300)
        self.historyTable.setItem(0, 0,QtWidgets.QTableWidgetItem("Hello"))
        self.historyTable.setItem(0, 1, QtWidgets.QTableWidgetItem("Hello"))
        self.historyTable.setItem(0, 2, QtWidgets.QTableWidgetItem("Hello"))

class PatientAppointment(QtWidgets.QMainWindow,Ui_PatientAppointment):
    __doctorId = ""
    __patientId = ""
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.requestButton.clicked.connect(self.requestAppointment)

    def requestAppointment(self):
        print(f"INSERT INTO appointment VALUES('meet_id','{self.prefferedDatetTime.dateTime().toPyDateTime()}','45hrs','{self.__patientId} {self.healthIssue.text()}','{self.__doctorId}','{self.__patientId}','{self.healthIssue.text()}')")

    def setIds(self,doctorid,patientId):
        self.__doctorId = doctorid
        self.__patientId = patientId

