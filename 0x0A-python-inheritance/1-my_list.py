#!/usr/bin/python3
"""A module that inherits from the list class"""


class MyList(list):
    """Inherits from a list"""
    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
