from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class ErrorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('error_window.ui', self)

        self.setWindowTitle("Ошибка")
        self.resize(285, 150)







