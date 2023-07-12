#!/usr/bin/python3
"""
Module for the function
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file

    Args:
        filename (str): file
        text (str): text
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
