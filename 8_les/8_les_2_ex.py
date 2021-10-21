class My_Zero_Division:
    def __init__(self, dividend, divisor):
        self.divident = dividend
        self.divisor = divisor
    @staticmethod
    def my_division(divident, divisor):
        try:
            return(f'{divident}/{divisor} = {divident/divisor}')
        except:
            return (f'{divident}/{divisor}\033[31m Division by Zero!!\033[0m')

a = My_Zero_Division(12, 1)
print(a.my_division(12, 0))
print(My_Zero_Division.my_division(13, 0))
print(My_Zero_Division.my_division(12, 1))
div = int(input('Enter divident: '))
divisor = int(input('Enter divisor: '))
print(My_Zero_Division.my_division(div, divisor))



