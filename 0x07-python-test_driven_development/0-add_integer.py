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
    def add_integer(a, b=98):
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer or b must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("a must be an integer or b must be an integer")

        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)

        return int(a + b)
