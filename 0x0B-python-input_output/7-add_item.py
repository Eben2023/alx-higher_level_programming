#!/usr/bin/python3
"""Module for add_items_to_list"""
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_items_to_list(filename, args):
    """
    Add the command-line arguments to a Python list and save it to a file.

    Args:
        filename (str): The name of the file to save the list to.
        args (List[str]): The command-line arguments to add to the list.

    Returns:
        None
    """

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    add_items_to_list("add_item.json", sys.argv[1:])
