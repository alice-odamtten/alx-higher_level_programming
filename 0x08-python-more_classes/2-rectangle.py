#!/usr/bin/python3
"""A module that defines a Rectangle class"""


class Rectangle:
    """a class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height
        Args:
        width : the width of a rectangle
        height : the height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
        value: the value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
        value : the value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__width == 0 or self.__height ==0:
            return (0)
        return (self.__width * 2) + (self.__heigh * 2)
