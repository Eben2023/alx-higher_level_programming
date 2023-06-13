#!/usr/bin/python3
"""Module for add_arguments_to_lists"""


import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_arguments_to_list(args):
    """
    Add all command-line arguments to a Python list.

    Args:
        args (list): The list of command-line arguments.

    Returns:
        list: The updated list with the added arguments.
    """

    # Load existing list from file if it exists
    if path.exists('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    else:
        my_list = []

    # Add arguments to the list
    my_list.extend(args)

    # Save the updated list to the file
    save_to_json_file(my_list, 'add_item.json')

    return my_list
