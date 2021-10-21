
class Warehouse:
    '''Класс Склад '''
    pass

class Office_Equipment:
    '''Класс Оргтехника'''
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'{self.name} Price: {self.price}. Quantity: {self.quantity}'

class Scanner(Office_Equipment):
    def scan(self):
        return f'My scanner {self.name} work!'
class Printer(Office_Equipment):
    def prin(self):
        return f'My printer {self.name} work!'
class Xerox(Office_Equipment):
    def xer(self):
        return f'My xerox {self.name} work!'

tech_1 = Scanner('Fijitsu', 12, 12000)
tech_2 = Printer('Canon', 11, 15000)
tech_3 = Xerox('Xerox', 5, 20000)
print(tech_1.scan())
print(tech_2.prin())
print(tech_3.xer())

