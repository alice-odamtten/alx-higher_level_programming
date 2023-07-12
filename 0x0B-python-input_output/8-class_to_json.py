#!/usr/bin/python3
"""
Module for the function
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure for JSON serialization
    of an object
    """
    return obj.__dict__
