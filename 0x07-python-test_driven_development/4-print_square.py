#!/usr/bin/python3
"""
This is module defines print_square function
"""


def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer or a float.
        ValueError: If `size` is less than 0.
        TypeError: If `size` is a float and is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
