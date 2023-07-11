#!/usr/bin/python3
"""
Module for the class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class
    """

    def __init__(self, size):
        """
        Instantiate with size

        Args:
            size (int)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
