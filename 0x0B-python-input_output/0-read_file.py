#!/usr/bin/python3

"""
This module provides a function to read and print
the contents of a text file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a text file.

    Args:
        filename (str): The name of the file to read.
        Defaults to an empty string.

    Returns:
        None
    """

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')


read_file("my_file_0.txt")
