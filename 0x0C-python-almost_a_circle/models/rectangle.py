#!/usr/bin/python3
""" Module defining the Rectangle class """


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class

        Args:
            width(int)
            height(int)
            x: initialized at zero
            y: initialized at zero
            id: initialized at none
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value: width value
        """
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value: height value
        """
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value: value of x
        """
        self.__x = value

    @property
    def y(self):
        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y attribute

        Args:
            value: value of y
        """
        self.__y = value
