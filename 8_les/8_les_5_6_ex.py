
class Office_Equipment:
    '''Класс Оргтехника'''

    def __init__(self, name, quantity, price, *args):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} Price: {self.price}. Quantity: {self.quantity}'

    def warehouse(self):
        try:
            unit = input(f'Enter name: ')
            unit_p = int(input(f'Enter price: '))
            unit_q = int(input(f'Enter quantity '))
            unique = {'Model:': unit, 'Price': unit_p, 'Quantity': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input()
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print(f'All Warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return Office_Equipment.warehouse(self)


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
print(tech_1.warehouse())
print(tech_2.warehouse())
print(tech_3.warehouse())
