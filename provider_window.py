from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class ProviderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('provider_window.ui', self)

        self.setWindowTitle("Поставщик")

        self.quitButton.clicked.connect(self.close)









