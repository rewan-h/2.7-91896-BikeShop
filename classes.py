# I normally put custom classes in seperate files to keep the main.py clean

class Rental:
    def __init__(self, name, rentalNum, bikeType, amount, startDate, endDate):
        self.name = str(name)
        self.rentalNum = int(rentalNum)
        self.bikeType = str(bikeType)
        self.amount = int(amount)
        self.startDate = startDate
        self.endDate = endDate

    def toTuple(self):
        return (
            self.name,
            self.rentalNum,
            self.bikeType,
            self.amount,
            self.startDate.strftime("%d/%m/%Y"),
            self.endDate.strftime("%d/%m/%Y")
        )