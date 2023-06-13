#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """
    Write the given string to a text file and return the number of
    characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to
        an empty string.
        text (str): The string to write to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters written to the file.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


nb_characters = write_file("my_first_file.txt",
                           "This School is so cool!\n")
