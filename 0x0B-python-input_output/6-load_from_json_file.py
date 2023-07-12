#!/usr/bin/python3
"""
Module for the function
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
