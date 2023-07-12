#!/usr/bin/python3
"""
Module for the function
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file

    Args:
        filename (str): file
        text (str): text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
