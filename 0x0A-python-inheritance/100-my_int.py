#!/usr/bin/python3

"""
Module for a class called MyInt.
"""


class MyInt(int):
    """
    Represents a rebel integer class.

    Public Methods:
        __eq__(self, other): Overrides the equality operator.
        __ne__(self, other): Overrides the inequality operator.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
