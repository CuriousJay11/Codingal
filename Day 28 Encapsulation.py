# encapsulation - security

class Mobile:
    def __init__(self):
        self.__price = 10000

    def sell(self):
        print(self.__price)

    def changeprice(self, price):
        self.price = price


mob = Mobile()
mob.sell()
mob.changeprice(8000)
mob.sell()
