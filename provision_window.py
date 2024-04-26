from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class ProvisionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('provision_window.ui', self)

        self.setWindowTitle("Поставка")

        self.quitButton.clicked.connect(self.close)









