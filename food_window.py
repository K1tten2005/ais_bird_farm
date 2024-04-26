from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow


class FoodWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('food_window.ui', self)

        self.setWindowTitle("Корм")

        self.quitButton.clicked.connect(self.close)









