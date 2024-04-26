from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class FeedingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('feeding_window.ui', self)

        self.setWindowTitle("Кормёжка")

        self.quitButton.clicked.connect(self.close)









