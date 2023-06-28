#!/usr/bin/python3

"""a class with private instance attribute"""


class Square:
    """a class square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiaization of an instance

        Args:
        size (int): The size of the square. Defaults to 0.
        position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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
        self.__size = value

    @property
    def position(self):
        """retrieves postion"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position

        Args:
        value (tuple): The position of the square.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position values must be positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """print # chracters
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
