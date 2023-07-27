#!/usr/bin/python3
"""
Module for Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Class Rectangle
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
