#!/usr/bin/python3
"""
Module for a class Rectangle
"""


class Rectangle:
    """
    A Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Class initializer

        Args:
            self : Argument
            width : Argument
            height : Argument

        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Width getter

        Args:
            self : Argument

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            self : Argument
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
        Height getter

        Args:
            self : Argument

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
            self : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method to return the biggest Rect based on area

        Args:
            rect_1 : Argument
            rect_2 : Argument

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size

        Args:
            cls : Argument
            size : Argument
                (default is 0)

        """
        return cls(size, size)

    def area(self):
        """
        Returns area

        Args:
            self : Argument

        """
        return self.height * self.width

    def perimeter(self):
        """
        Returns perimeter

        Args:
            self : Argument

        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        Returns rectangle with a string

        Args:
            self : Argument

        """
        if self.height == 0 or self.width == 0:
            return ""
        square = ""
        for i in range(self.height):
            for j in range(self.width):
                square += str(self.print_symbol)
            if i != self.height - 1:
                square += "\n"
        return square

    def __repr__(self):
        """
        Returns a string representation of the rectangle

        Args:
            self : Argument

        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a msg when an instance of Rectangle is deleted

        Args:
            self : Argument

        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
