#!/usr/bin/python3
"""Module for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of the given object to a text file.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
