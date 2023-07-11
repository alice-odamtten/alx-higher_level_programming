#!/usr/bin/python3
"""
A module of the function
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class.

    Args:
        obj: the object
        a_class: the class
    """
    return type(obj) == a_class
