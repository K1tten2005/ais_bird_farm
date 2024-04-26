from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication




class CreatorInfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('creator_info_window.ui', self)


        self.setWindowTitle("О разработчике")

        self.quitButton.clicked.connect(self.close)






