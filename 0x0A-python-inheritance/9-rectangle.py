#!/usr/bin/python3
"""
Module for the class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class
    """

    def __init__(self, width, height):
        """
        Instantiation of width and height

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns rectangle description
        """
        return ("[" + type(self).__name__ + "] " + str(self.__width)
                + "/" + str(self.__height))
