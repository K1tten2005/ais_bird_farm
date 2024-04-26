from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class CustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('customer_window.ui', self)

        self.setWindowTitle("Заказчик")

        self.quitButton.clicked.connect(self.close)









