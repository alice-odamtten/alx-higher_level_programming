#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers"""
    prev = 0
    for i, j in enumerate(list_of_integers):
        if i:
            prev = list_of_integers[i - 1]
        if i < len(list_of_integers) - 1:
            next = list_of_integers[i + 1]
        else:
            next = 0
        if j >= prev and j >= next:
            return j
