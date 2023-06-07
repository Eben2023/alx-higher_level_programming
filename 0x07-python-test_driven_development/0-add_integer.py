#!/usr/bin/python3
"""
A function that adds to numbers a, b=98
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer. Default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
