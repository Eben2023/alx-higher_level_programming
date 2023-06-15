#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """Base class for generating unique identifiers."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize an instance of Base.

        Args:
            id (int, optional): Identifier value (default: None).
                If provided, assign the value to the public instance
                attribute `id`. If not provided, increment `__nb_objects`
                and assign the new value to the `id` attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
