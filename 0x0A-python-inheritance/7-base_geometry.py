#!/usr/bin/python3
"""
Module for BaseGeometry
"""


class BaseGeometry:
    """
    A Class with public instance methods
    """

    def area(self):
        """
        Raise an Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates the value

        Args:
            name (str)
            value (int)
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
