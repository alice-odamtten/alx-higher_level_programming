#!/usr/bin/python3
"""
A module for the function inherits_from
"""


def inherits_from(obj, a_class):
    """
    A function that returns True if the object is an instance
    of a class that inherited.

    Args:
        obj: object
        a_class: class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
