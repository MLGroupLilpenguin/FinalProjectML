from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox

from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee
from retail_project.uis.EmployeeMainWindow import Ui_MainWindow


class EmployeeMainWindowEx(Ui_MainWindow):
    def __int__(self):
        self.es = EmployeeConnector()
        self.ec.connect()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.displayEmployeeIntoTable()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def displayEmployeeIntoTable(self):
        self.employees=self.ec.get_all_employees()
        self.tableWidgetEmployee.setRowCount(0)
        for emp in self.employees:
            #lấy dòng cuối cùng ( nối đuôi vào)
            row = self.tableWidgetEmployee.RowCount(0)
            # chèn dòng mới
            self.tableWidgetEmployee.insertRow(row)
            #insert data for id column
            item_id = QTableWidgetItem(str(emp.ID))
            self.tableWidgetEmployee.setItem(row, 0, item_id)
            #Code:
            item_code = QTableWidgetItem(str(emp.EmployeeCode))
            self.tableWidgetEmployee.setItem(row, 1, item_code)
            #Name
            item_name = QTableWidgetItem(str(emp.Name))
            self.tableWidgetEmployee.setItem(row, 2, item_name)
            #phone
            item_phone = QTableWidgetItem(str(emp.Phone))
            self.tableWidgetEmployee.setItem(row, 3, item_phone)
            #emaik
            item_email = QTableWidgetItem(str(emp.Email))
            self.tableWidgetEmployee.setItem(row, 4, item_email)
    def setupSignalAndSlot(self):
        self.pushButtonNew.clicked.connect(self.clear_all)
        self.tableWidgetEmployee.itemSelectionChanged.connect(self.show_detail)
    def clear_all(self):
        self.lineEditId.setText("")
        self.lineEditCode.clear()
        self.lineEditName.setText("")
        self.lineEditPhone.setText("")
        self.lineEditEmail.setText("")
        self.lineEditCode.setFocus()
    def show_detail(self):
        row_index = self.tableWidgetEmployee.currentIndex()
        print("you clicked at", row_index)
        id = self.tableWidgetEmployee.item(row_index, 0).text()
        print(id)
        emp=self.ec.get_detail_infor(id)
        if emp != None:
            self.lineEditId.setText(str(emp.ID))
            self.lineEditCode.setText(str(emp.EmployeeCode))
            self.lineEditName.setText(str(emp.Name))
            self.lineEditPhone.setText(str(emp.Phone))
            self.lineEditEmail.setText(str(emp.Email))
            if emp.IsDeleted ==1:
                self.checkBoxIsDeleted.setChecked(True)
            else:
                self.checkBoxIsDeleted.setChecked(False)
    def save_employee(self):
        emp = Employee()
        emp.EmployeeCode = self.lineEditId.text().text()
        emp.Name = self.lineEditName.text().text()
        emp.Phone = self.lineEditPhone.text().text()
        emp.Email = self.lineEditEmail.text().text()
        emp.Password = self.lineEditPassword.text()
        emp.IsDeleted = 0
        result = self.ec.insert_employee(emp)
        if result > 0:
            self.displayEmployeeIntoTable()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed, please check your account again")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()