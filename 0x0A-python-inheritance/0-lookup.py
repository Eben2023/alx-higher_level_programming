#!/usr/bin/python3
"""
    This module provides a function that retrieves the list of attributes
    and methods available in an object.
"""


def lookup(obj):
    """Retrieves the attributes and methods of an object."""
    return dir(obj)
