#!/usr/bin/python3
"""
Module for the function
"""


def read_file(filename=""):
    """
    A function that reads a text file and prints it

    Args:
        filename (str): ""
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end='')
