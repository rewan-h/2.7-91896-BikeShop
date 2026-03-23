# I normally put custom classes in seperate files to keep the main.py clean
from random import randint


class Rental:
    def __init__(self, name, rentalNum, bikeType, amount, startDate, endDate):
        self.name = str(name)
        self.rentalNum = int(rentalNum)
        self.bikeType = str(bikeType)
        self.amount = int(amount)
        self.startDate = startDate
        self.endDate = endDate
        self.raffleNum = int(randint(1,150))