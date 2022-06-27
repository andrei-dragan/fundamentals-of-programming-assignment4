from src.services.services import Services


class ComplexUI:
    def __init__(self):
        self.__services = Services()

    def __menu(self):
        print('\nHello there! Choose a command:')
        print('1 - to add a number')
        print('2 - to display the list of numbers')
        print('3 - to filter the list of numbers by keeping only the numbers from <start> to <end>')
        print('4 - to undo the last operation')
        print('5 - to exit\n')

    def start(self):
        self.__services.generate_numbers(10)

        while True:
            try:
                self.__menu()
                try:
                    command = int(input('Enter the command: '))
                    if command < 1 or command > 5:
                        raise ValueError('Invalid Input!')
                except ValueError:
                    raise ValueError('Invalid Input!')

                if command == 1:
                    try:
                        real = int(input('Enter the real part: '))
                    except ValueError:
                        raise ValueError('Invalid real part!')

                    try:
                        imaginary = int(input('Enter the imaginary part: '))
                    except ValueError:
                        raise ValueError('Invalid imaginary part!')

                    self.__services.add_number(real, imaginary)

                elif command == 2:
                    print(str(self.__services))

                elif command == 3:
                    try:
                        start = int(input('Enter start position: '))
                    except ValueError:
                        raise ValueError('Invalid start position!')

                    try:
                        end = int(input('Enter end position: '))
                    except ValueError:
                        raise ValueError('Invalid end position!')

                    self.__services.filter_numbers(start, end)

                elif command == 4:
                    self.__services.undo()

                elif command == 5:
                    return

                else:
                    raise ValueError('Invalid Input!')

            except ValueError as ve:
                print(ve)



