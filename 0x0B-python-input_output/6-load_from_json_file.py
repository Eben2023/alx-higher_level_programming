#!/usr/bin/python3
"""Module for load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file and return it.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        object: The Python object loaded from the JSON file.
    """

    with open(filename, 'r') as file:
        return json.load(file)
