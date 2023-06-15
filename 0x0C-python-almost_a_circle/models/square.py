#!/usr/bin/python3

"""
This module defines the Square class that inherits from the Rectangle class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class represents a square and inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method to retrieve the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance.
        """
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square instance.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
