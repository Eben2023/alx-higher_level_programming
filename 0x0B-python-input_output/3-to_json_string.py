#!/usr/bin/python3
"""Module for to_json_string"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of the given object as a string.

    Args:
        my_obj: The object to be serialized into JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """

    return json.dumps(my_obj)
