class My_Error:
    def __init__(self, *args):
        self.my_list = []

    def input_list(self):
        while True:
            try:
                el = int(input('Enter your number:'))
                self.my_list.append(el)
                print(f'My_list now: {self.my_list}\n')
            except:
                print(f'Bad value There should only be numbers')
                try_again = input('Try again? Y/N ')
                if try_again == 'Y':
                    print(try_except.input_list())
                else:
                    if try_again == 'N':
                        return f'Goodbye! Stop'
                        break
                    else:
                        return f'Goodbye'
                        break


try_except = My_Error(1)
print(try_except.input_list())
