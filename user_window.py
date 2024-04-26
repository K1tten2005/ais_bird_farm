from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('user_window.ui', self)

        self.setWindowTitle("Пользователь")

        self.quitButton.clicked.connect(self.close)









