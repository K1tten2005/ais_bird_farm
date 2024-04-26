from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QLineEdit

from creator_info_window import CreatorInfoWindow
from admin_window import AdminWindow
from user_window import UserWindow
from worker_window import WorkerWindow
from error_window import ErrorWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)

        self.setWindowTitle("Птицеферма")

        self.creatorInfoButton.clicked.connect(self.creatorInfoButton_clicked)

        #Quit buttons
        #creator_info
        self.creator_info_window = CreatorInfoWindow()
        self.creator_info_window.quitButton.clicked.connect(self.creatorInfo_quitButton_clicked)
        #worker
        self.worker_window = WorkerWindow()
        self.worker_window.quitButton.clicked.connect(self.worker_quitButton_clicked)
        #user
        self.user_window = UserWindow()
        self.user_window.quitButton.clicked.connect(self.user_quitButton_clicked)
        #admin
        self.admin_window = AdminWindow()
        self.admin_window.quitButton.clicked.connect(self.admin_quitButton_clicked)

        self.quitButton.clicked.connect(self.quitButton_clicked)

        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.logInButton.clicked.connect(self.logInButton_clicked)

    def creatorInfoButton_clicked(self):
        self.creator_info_window.show()
        self.hide()

    def creatorInfo_quitButton_clicked(self):
        self.show()

    def worker_quitButton_clicked(self):
        self.show()
    def user_quitButton_clicked(self):
        self.show()

    def admin_quitButton_clicked(self):
        self.show()

    def quitButton_clicked(self):
        self.close()

    def logInButton_clicked(self):
        login = self.loginLineEdit.text()
        password = self.passwordLineEdit.text()
        if login == 'admin' and password == 'admin':
            self.admin_window.show()
            self.close()
        elif login == 'user' and password == 'user':
            self.user_window.show()
            self.close()
        elif login == 'worker' and password == 'worker':
            self.worker_window.show()
            self.close()

        else:
            self.error_window = ErrorWindow()
            self.error_window.show()
            print('Wrong login or password!')







