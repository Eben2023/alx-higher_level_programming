#!/usr/bin/python3

"""
Write a class Rectangle that inherits from BaseGeometry.

Instantiation with width and height: def __init__(self, width, height)
width and height must be private. No getter or setter.
width and height must be positive integers, validated by integer_validator.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
