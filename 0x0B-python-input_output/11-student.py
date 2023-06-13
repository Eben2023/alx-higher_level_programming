#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve (default: None).

        Returns:
            dict: A dictionary representation of the Student instance.
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based on a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.
        """

        for attr, value in json.items():
            setattr(self, attr, value)
