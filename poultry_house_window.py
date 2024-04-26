from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class PoultryHouseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('poultry_house_window.ui', self)

        self.setWindowTitle("Птичник")

        self.quitButton.clicked.connect(self.close)









