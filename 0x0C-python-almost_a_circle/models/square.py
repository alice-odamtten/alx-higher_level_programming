#!/usr/bin/python3
""" Module defining the Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method for Square class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return a string representing the square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
