#!/usr/bin/python3
"""Checks if an object is exactly an instance"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        False otherwise.
    """
    return type(obj) == a_class
