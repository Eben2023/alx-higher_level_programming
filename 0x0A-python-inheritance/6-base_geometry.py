#!/usr/bin/python3

"""
This module contains the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class represents a basic geometry class.
    It serves as a base class for other geometry classes.

    Public Methods:
        area(self): Raises an Exception with the message "area()
        is not implemented"
    """
    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
            Exception: Always raises an Exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
