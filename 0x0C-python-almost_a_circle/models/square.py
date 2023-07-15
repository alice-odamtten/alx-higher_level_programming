#!/usr/bin/python3
""" Module defining the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ method for Square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Get the size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size attribute """
        self.width = value
        self.height = value

    @property
    def width(self):
        """ Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value: width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value: height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def __str__(self):
        """ Return representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width,
                                                 self.height)

    def update(self, *args, **kwargs):
        """ Updating the attributes of square """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
