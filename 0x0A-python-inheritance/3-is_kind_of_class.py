#!/usr/bin/python3

"""
This module contains a function to check if an object is an
instance of,or if the object is an instance of a class that
inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object
    is an instance of a class that inherited from, the
    specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the
        specified class; False otherwise.
    """
    return isinstance(obj, a_class)
