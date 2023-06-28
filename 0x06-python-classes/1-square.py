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
