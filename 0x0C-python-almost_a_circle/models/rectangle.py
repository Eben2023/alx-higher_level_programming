#!/usr/bin/python3

"""
This module defines the Rectangle class that inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class represents a rectangle and inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x-coordinate attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y-coordinate attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character '#'."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def display(self):
        """Print the Rectangle instance with the character '#'."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args):
        """Assign arguments to the attributes of the Rectangle instance."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """
        Assign arguments or key-value pairs to the attributes
        of the Rectangle instance.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle instance.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
