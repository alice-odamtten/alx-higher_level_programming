#!/usr/bin/python3
"""
Module for the function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file

    Args:
        my_obj (obj): content
        filename (str): file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
