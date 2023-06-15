#!/usr/bin/python3

"""
This module defines the Base class that serves as
the base class for other classes.
"""

import json
import csv
import turtle


class Base:
    """
    Base class serves as the base class for other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        data = []
        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json file."""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        row = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        }
                    elif cls.__name__ == "Square":
                        dictionary = {
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        }
                    instance = cls.create(**dictionary)
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares."""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")
        pen = turtle.Turtle()

        def draw_shape(shape, color):
            pen.penup()
            pen.setposition(shape.x, shape.y)
            pen.pendown()
            pen.color(color)
            if isinstance(shape, Rectangle):
                for _ in range(2):
                    pen.forward(shape.width)
                    pen.right(90)
                    pen.forward(shape.height)
                    pen.right(90)
            elif isinstance(shape, Square):
                for _ in range(4):
                    pen.forward(shape.size)
                    pen.right(90)

        for rectangle in list_rectangles:
            draw_shape(rectangle, "red")

        for square in list_squares:
            draw_shape(square, "blue")

        turtle.done()
