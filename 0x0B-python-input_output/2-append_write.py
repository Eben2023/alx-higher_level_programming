#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """
    Append the given string to the end of a text file and return the
    number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to
        an empty string.
        text (str): The string to append to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters added to the file.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
