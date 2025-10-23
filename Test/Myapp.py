from PyQt6.QtWidgets import QApplication, QMainWindow

from UIUX.MaincustomerEX import MainWindowEx

app=QApplication([])
customer_ui=MainWindowEx()
customer_ui.setupUi(QMainWindow())
customer_ui.showWindow()
app.exec()