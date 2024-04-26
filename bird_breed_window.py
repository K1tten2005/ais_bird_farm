from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class BirdBreedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('bird_breed_window.ui', self)

        self.setWindowTitle("Порода птицы")

        self.quitButton.clicked.connect(self.close)









