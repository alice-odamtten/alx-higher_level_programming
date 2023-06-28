#!/usr/bin/python3

"""a class with private instance attribute"""


class Square:
    """a class square that defines a square"""

    def __init__(self, size):
        """Initiaization of an instance

        Args:
        size(int):size of a square
        """
        self.__size = size

    @property
    def size(self):
        """ get size property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set method to square size

        Args:
        value(int):size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the current square area
        """
        return self.__size ** 2
