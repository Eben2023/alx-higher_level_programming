#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    Args:
        obj (object): An instance of a class.

    Returns:
        dict: The dictionary description of the object for JSON serialization.
    """

    return obj.__dict__
