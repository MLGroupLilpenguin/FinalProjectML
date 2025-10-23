from UIUX.MainCustomer import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.ProfileBut.clicked.connect(lambda: self.switch_page(0))
        self.OrderBut.clicked.connect(lambda: self.switch_page(1))
        self.OrderHistoryBut.clicked.connect(lambda: self.switch_page(2))
        self.stackedWidget.setCurrentIndex(0)
        MainWindow.setStyleSheet("""
               QMainWindow, QWidget {
                   background-color: #1e1e1e;   /* Nền đen kiểu VS Code */
                   color: white;               /* Chữ trắng */
               }
               QPushButton {
                   background-color: #2d2d2d;
                   color: white;
                   border-radius: 4px;
                   padding: 6px;
               }
               QPushButton:hover {
                   background-color: #3a3a3a;
               }
               QPushButton:pressed {
                   background-color: #4a4a4a;
               }
               QGroupBox {
                   border: 1px solid #555;
                   margin-top: 10px;
               }
               QLineEdit, QComboBox {
                   background-color: #2a2a2a;
                   color: white;
                   border: 1px solid #444;
               }
               QLabel {
                   color: white;
               }
           """)
    def switch_page(self, index: int):
        self.stackedWidget.setCurrentIndex(index)
        # Làm nổi bật nút đang chọn (tuỳ chọn)
        buttons = [self.Profile, self.Order, self.Orderhistory]
        for i, btn in enumerate(buttons):
            if i == index:
                btn.setStyleSheet("background-color: lightblue; font-weight: bold;")
            else:
                btn.setStyleSheet("")


    def showWindow(self):
        self.MainWindow.show()