#!/usr/bin/python3
"""
Module of the function lookup()
"""


def lookup(obj):
    """
    A function that returns the list of
    available attributes

    Args:
        obj
    """
    return dir(obj)
