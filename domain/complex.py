class Complex:
    def __init__(self, real, imaginary):
        """
        Constructor for Complex class
        :param real: The real part of the complex number
        :param imaginary: The imaginary part of the complex number
        """
        self.__real = real
        self.__imaginary = imaginary

    @property
    def real(self):
        return self.__real

    # @real.setter
    # def real(self, new_value):
    #    self.__real = new_value

    @property
    def imaginary(self):
        return self.__imaginary

    # @imaginary.setter
    # def imaginary(self, new_value):
    #     self._imaginary = new_value

    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        elif self.real == 0 and self.imaginary != 0:
            return str(self.imaginary) + "i"
        else:
            if self.imaginary > 0:
                return str(self.real) + "+" + str(self.imaginary) + "i"
            else:
                return str(self.real) + str(self.imaginary) + "i"
