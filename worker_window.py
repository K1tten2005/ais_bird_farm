from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class WorkerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('worker_window.ui', self)

        self.setWindowTitle("Сотрудник")

        self.quitButton.clicked.connect(self.close)







