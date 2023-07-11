#!/usr/bin/python3
"""
Module of the class
"""


class MyList(list):
    """
    A class that inherits from list
    """

    def print_sorted(self):
        """
        A function that prints the list, but sorted

        Args:
            self
        """
        print(sorted(self))
