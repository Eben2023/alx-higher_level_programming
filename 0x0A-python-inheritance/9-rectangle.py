#!/usr/bin/python3

"""
Module for a class called Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.

    Public Methods:
        __init__(self, width, height): Initializes a Rectangle instance.
        area(self): Calculates the area of the rectangle.
        __str__(self): Returns the string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The rectangle description in the format [Rectangle]
            <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
