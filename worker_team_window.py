from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class WorkerTeamWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('worker_team_window.ui', self)

        self.setWindowTitle("Бригада")

        self.quitButton.clicked.connect(self.close)







