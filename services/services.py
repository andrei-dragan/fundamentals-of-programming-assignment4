from random import randrange
from src.domain.complex import Complex


class Services:
    def __init__(self):
        """
        Constructor for Services class
        We have the current list of numbers
        And the list of lists, representing the undo states
        """
        self.__numbers = []
        self.__undo_list = []

    def generate_numbers(self, n):
        """
        Generate n random complex numbers
        :param n: How many numbers to create
        :return: None
        """
        for i in range(n):
            self.__numbers.append(Complex(randrange(500), randrange(500)))
        self.__add_undo()

    def __copy_list(self):
        """
        Copies the current list into a new one, with a changed reference
        :return: The new referenced list
        """
        new_numbers = []
        for number in self.__numbers:
            new_numbers.append(number)
        return new_numbers

    def __add_undo(self):
        """
        Add to the undo_list the current state of the list of numbers
        :return: None
        """
        new_undo_list = self.__copy_list()
        self.__undo_list.append(new_undo_list)

    def __get_number_from_list(self, x):
        """
        Get the number from the number's list on the position x
        :param x: The position in the list we want to get the number from
        :return: The number from position x
        """
        return self.__numbers[x]

    def filter_numbers(self, start, end):
        """
        Filter the number's list and keep the ones only between start and end
        :param start: The position from we want to keep numbers
        :param end: The position until we want to keep numbers
        :return: None
        """

        length = len(self.__numbers)
        if start < 1 or start > length:
            raise ValueError('Invalid start position!')

        if end < 1 or end > length or end < start:
            raise ValueError('Invalid end position!')

        self.__add_undo()

        new_numbers = []
        for i in range(start - 1, end):
            new_numbers.append(self.__get_number_from_list(i))

        self.__numbers = new_numbers

    def add_number(self, real, imaginary):
        """
        Add a complex number to the list
        :param real: The real part of the complex number
        :param imaginary: The imaginary part of the complex number
        :return: None
        """
        number = Complex(real, imaginary)
        self.__add_undo()
        self.__numbers.append(number)

    def undo(self):
        """
        Set the actual list of numbers to the previous state (if it existed)
        :return: None
        """
        if len(self.__undo_list) > 0:
            self.__numbers = self.__undo_list[-1]
            self.__undo_list.pop()

    @property
    def numbers(self):
        return self.__numbers

    def __str__(self):
        answer = ''
        for number in self.numbers:
            answer += str(number) + ', '
        answer = answer[0:-2]
        return answer


def test_generate_numbers():
    services = Services()
    services.generate_numbers(10)

    length = len(services.numbers)
    assert length == 10

    for number in services.numbers:
        real = number.real
        imaginary = number.imaginary
        assert 0 <= real < 500 and 0 <= imaginary < 500


test_generate_numbers()


def test_add_number():
    services = Services()
    services.add_number(5, 10)
    services.add_number(15, 15)
    services.add_number(-3, 0)

    assert services.numbers[0].real == 5 and services.numbers[0].imaginary == 10
    assert services.numbers[1].real == 15 and services.numbers[1].imaginary == 15
    assert services.numbers[2].real == -3 and services.numbers[2].imaginary == 0


test_add_number()


def test_filter_numbers():
    services = Services()

    services.add_number(1, 1)
    services.add_number(10, 12)
    services.add_number(16, -3)
    services.add_number(4, 5)
    services.add_number(0, 1)

    services.filter_numbers(2, 4)

    assert services.numbers[0].real == 10 and services.numbers[0].imaginary == 12
    assert services.numbers[1].real == 16 and services.numbers[1].imaginary == -3
    assert services.numbers[2].real == 4 and services.numbers[2].imaginary == 5


test_filter_numbers()


def test_undo():
    services = Services()

    services.add_number(1, 1)
    services.add_number(10, 12)
    services.add_number(16, -3)
    services.add_number(4, 5)
    services.add_number(0, 1)

    services.undo()
    services.add_number(5, 15)

    assert services.numbers[4].real == 5 and services.numbers[4].imaginary == 15

    services.undo()
    assert len(services.numbers) == 4
    assert services.numbers[3].real == 4 and services.numbers[3].imaginary == 5


test_undo()
