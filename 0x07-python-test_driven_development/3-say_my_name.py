#!/usr/bin/python3
"""Module to print a name"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints firstname with lastname

    Args:
        first_name :First name
        last_name : Last name

    Raises:
        TypeError: If first_name or last_name is not a string
        ValueError: first_name must not be empty

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name != "":
        full_name = f"My name is {first_name} {last_name}"
    else:
        full_name = f"My name is {first_name}"

    print(full_name)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
