from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
from bird_breed_window import BirdBreedWindow
from customer_window import CustomerWindow
from feeding_window import FeedingWindow
from food_window import FoodWindow
from poultry_house_window import PoultryHouseWindow
from provider_window import ProviderWindow
from provision_window import ProvisionWindow
from worker_window import WorkerWindow
from worker_team_window import WorkerTeamWindow

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('admin_window.ui', self)

        self.setWindowTitle("Админ")

        self.quitButton.clicked.connect(self.close)

        # bird breed
        self.birdBreedButton.clicked.connect(self.birdBreedButton_clicked)
        self.bird_breed = BirdBreedWindow()
        self.bird_breed.quitButton.clicked.connect(self.bird_breed_quitButton_clicked)

        # customer
        self.customerButton.clicked.connect(self.customerButton_clicked)
        self.customer = CustomerWindow()
        self.customer.quitButton.clicked.connect(self.customer_quitButton_clicked)

        # feeding
        self.feedingButton.clicked.connect(self.customerButton_clicked)
        self.feeding = FeedingWindow()
        self.feeding.quitButton.clicked.connect(self.feeding_quitButton_clicked)

        # food
        self.foodButton.clicked.connect(self.foodButton_clicked)
        self.food = FoodWindow()
        self.food.quitButton.clicked.connect(self.food_quitButton_clicked)

        # poultry_house
        self.poultryHouseButton.clicked.connect(self.poultryHouseButton_clicked)
        self.poultry_house = PoultryHouseWindow()
        self.poultry_house.quitButton.clicked.connect(self.poultry_house_quitButton_clicked)

        # provider
        self.providerButton.clicked.connect(self.providerButton_clicked)
        self.provider = ProviderWindow()
        self.provider.quitButton.clicked.connect(self.provider_quitButton_clicked)

        # provision
        self.provisionButton.clicked.connect(self.provisionButton_clicked)
        self.provision = ProvisionWindow()
        self.provision.quitButton.clicked.connect(self.provision_quitButton_clicked)

        # worker
        self.workerButton.clicked.connect(self.workerButton_clicked)
        self.worker = WorkerWindow()
        self.worker.quitButton.clicked.connect(self.worker_quitButton_clicked)

        # worker_team
        self.workerTeamButton.clicked.connect(self.workerTeamButton_clicked)
        self.worker_team = WorkerTeamWindow()
        self.worker_team.quitButton.clicked.connect(self.worker_team_quitButton_clicked)

    # FUNCS
    # bird_breed
    def bird_breed_quitButton_clicked(self):
        self.show()

    def birdBreedButton_clicked(self):
        self.hide()
        self.bird_breed.show()

    # customer
    def customerButton_clicked(self):
        self.hide()
        self.customer.show()

    def customer_quitButton_clicked(self):
        self.show()

    # feeding
    def feedingButton_clicked(self):
        self.hide()
        self.feeding.show()

    def feeding_quitButton_clicked(self):
        self.show()

    # food
    def foodButton_clicked(self):
        self.hide()
        self.food.show()
    def food_quitButton_clicked(self):
        self.show()

    # poultry_house
    def poultryHouseButton_clicked(self):
        self.hide()
        self.poultry_house.show()
    def poultry_house_quitButton_clicked(self):
        self.show()

    # provider
    def providerButton_clicked(self):
        self.hide()
        self.provider.show()
    def provider_quitButton_clicked(self):
        self.show()

    # provision
    def provisionButton_clicked(self):
        self.hide()
        self.provision.show()
    def provision_quitButton_clicked(self):
        self.show()

    # worker
    def workerButton_clicked(self):
        self.hide()
        self.worker.show()
    def worker_quitButton_clicked(self):
        self.show()

    # worker_team
    def workerTeamButton_clicked(self):
        self.hide()
        self.worker_team.show()
    def worker_team_quitButton_clicked(self):
        self.show()





