#!/usr/bin/python3
"""
Define a class Square that represents a square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two squares are equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if two squares are not equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if the current square is smaller than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if the current square is smaller than or equal to the other
        square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is smaller or equal, False
            otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Check if the current square is greater than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if the current square is greater than or equal to the other
        square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater or equal, False
            otherwise.
        """
        return self.area() >= other.area()
