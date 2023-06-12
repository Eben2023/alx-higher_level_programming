#!/usr/bin/python3

"""
Module for a class called BaseGeometry.
"""


class BaseGeometry:
    """
    Represents a base geometry class.

    Public Methods:
        area(self): Raises an Exception indicating that the method is not implemented.
        integer_validator(self, name, value): Validates a value as an integer.
    """

    def area(self):
        """
        Calculates the area of the geometry object.

        Raises:
            Exception: Indicates that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
