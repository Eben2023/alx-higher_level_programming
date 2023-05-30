#!/usr/bin/python3

"""
This module defines the Square class.

The Square class represents a square shape. It allows instantiation with a size
and provides an attribute to access the size value.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
