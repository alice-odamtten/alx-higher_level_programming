#!/usr/bin/python3
"""
Module to create a class Rectangle
"""


class Rectangle:
    """
    A class that represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the class

        Args:
            width : the width of the rectangle
            height : the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle

        Args:
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle

        Args:
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        Prints the character # as string
        """
        if self.height == 0 or self.width == 0:
            return ""
        square = ""
        for i in range(self.height):
            for j in range(self.width):
                square += "#"
            if i != self.height - 1:
                square += "\n"
        return square

    def __repr__(self):
        """
        Representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes the rectangle
        """
        print("Bye rectangle...")
