import dataclasses


class Data:
    def __init__(self, my_data):
        self.my_data = str(my_data)

    @classmethod
    def data_to_number(cls, my_data):
        result_data_to_number = []

        for i in my_data.split():
            if i != '-':
                result_data_to_number.append(i)
        return int(result_data_to_number[0]), int(result_data_to_number[1]), int(result_data_to_number[2])

    @staticmethod
    def examination(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'\033[32mGood data!\033[0m'
                else:
                    return f'\033[31mYear can only be it 0 to 2021\033[0m'
            else:
                return f'\033[31mMonth can only be it 1 to 12\033[0m'
        else:
            return f'\033[31mDay can only be it 1 to 31\033[0m'

    def __str__(self):
        return f'My_data {Data.data_to_number(self.my_data)}'


my_data = Data('21 - 10 - 2021')
print(my_data)
print(Data.examination(21, 10, 2022))
print(my_data.examination(21, 13, 2021))
print(my_data.examination(32, 10, 2021))
print(Data.data_to_number('21 - 10 - 2021'))
print(my_data.data_to_number('21 - 10 - 2021'))
print(Data.examination(21, 10, 2021))
