#!/usr/bin/python3

"""
Module for a class called Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square shape.

    Public Methods:
        __init__(self, size): Initializes a Square instance.
        area(self): Calculates the area of the square.
        __str__(self): Returns the string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with specified size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: The square description in the format [Rectangle]
            <size>/<size>.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
