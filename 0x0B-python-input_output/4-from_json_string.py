#!/usr/bin/python3
"""Module for from_json_string"""
import json


def from_json_string(my_str):
    """
    Return the Python data structure represented by the given JSON string.

    Args:
        my_str (str): The JSON string to be parsed.

    Returns:
        object: The Python data structure represented by the JSON string.
    """

    return json.loads(my_str)
