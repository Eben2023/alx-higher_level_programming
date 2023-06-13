#!/usr/bin/python3
"""Module for append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matching
        line.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """

    try:
        with open(filename, 'r+') as file:
            lines = file.readlines()
            file.seek(0)

            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

            file.truncate()

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' does not exist.")
