# I normally put custom classes in seperate files to keep the main.py clean
from random import randint


class Rental:
    def __init__(self, name, rentalNum, bikeType, amount, startDate, endDate):
        self.name = name
        self.rentalNum = rentalNum
        self.bikeType = bikeType
        self.amount = amount
        self.startDate = startDate
        self.endDate = endDate
        self.raffleNum = randint(1,150)