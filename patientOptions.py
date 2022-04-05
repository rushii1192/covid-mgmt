
from frontend.patientHistoryWindow import Ui_PatientHistory
from frontend.patientAppointmentWindow import Ui_PatientAppointment
from PyQt5 import QtWidgets,QtGui
from backend import DatabaseConnection
class PatientHistory(QtWidgets.QMainWindow,Ui_PatientHistory):
    __patientId = ""
    __dc = DatabaseConnection()
    __cursor = __dc.cursor()
    def __init__(self,patientId) -> None:
        super().__init__()
        self.setupUi(self)
        currentRow = self.historyTable.rowCount()
        self.historyTable.verticalHeader().setVisible(False)
        self.historyTable.horizontalHeader().setVisible(False)
        self.historyTable.setColumnCount(3)
        self.historyTable.setRowCount(10)
        self.__patientId = patientId
        self.historyTable.insertRow(currentRow)
        self.historyTable.setColumnWidth(0, 250)
        self.historyTable.setColumnWidth(1, 250)
        self.historyTable.setColumnWidth(2, 250)

        self.__cursor.execute(f"SELECT * FROM appointment WHERE PatientId = '{self.__patientId}';")
        result = self.__cursor.fetchall()
        for count, row in enumerate(result):
            self.historyTable.setItem(count, 0, QtWidgets.QTableWidgetItem(f'{row[4]}'))
            self.historyTable.setItem(count, 1, QtWidgets.QTableWidgetItem(f'{row[-1]}'))
            self.historyTable.setItem(count, 2, QtWidgets.QTableWidgetItem(f'{row[1]}'))

class PatientAppointment(QtWidgets.QMainWindow,Ui_PatientAppointment):
    __doctorId = ""
    __patientId = ""
    __dc = DatabaseConnection()
    __cursor = __dc.cursor()
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.requestButton.clicked.connect(self.requestAppointment)

    def requestAppointment(self):
        self.__cursor.execute(f"INSERT INTO appointment VALUES('meet_id','{self.prefferedDatetTime.dateTime().toPyDateTime()}','45hrs','{self.__patientId} {self.healthIssue.text()}','{self.__doctorId}','{self.__patientId}','{self.healthIssue.text()}')")
        self.__dc.commit()
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle('Successfull')
        msg.setText(f'Your appointment has been sent to doctor.')
        msg.setStyleSheet('color:black')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def setIds(self,doctorid,patientId):
        self.__doctorId = doctorid
        self.__patientId = patientId

