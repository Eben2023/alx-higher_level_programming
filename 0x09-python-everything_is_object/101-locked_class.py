#!/usr/bin/python3

"""
This module defines a LockedClass that prevents dynamic creation of
instance attributes,
except for 'first_name'.
"""


class LockedClass:
    """
    Class that prevents dynamic creation of instance attributes,
    except for 'first_name'.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """
        Initializes a new instance of LockedClass.
        """
        pass
