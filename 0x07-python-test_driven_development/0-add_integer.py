#!/usr/bin/python3
"""module to add two integers"""


def add_integer(a, b=98):
    """fuction to add integers, when the argument is float
    it convert it to integer

    Args:
       a(int): first integer
       b(int): second integer set to default 98

    Returns: the addition of a and b

    Raises:
    TypeError: a and b must be either float or integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
