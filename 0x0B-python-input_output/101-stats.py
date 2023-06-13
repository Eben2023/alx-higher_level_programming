#!/usr/bin/python3
"""Module for print_metrics"""
import sys


def print_metrics(status_codes, total_size):
    """
    Print the computed metrics based on the provided statistics.

    Args:
        status_codes (dict): A dictionary containing the status codes and their counts.
        total_size (int): The total file size.

    Returns:
        None
    """

    print("File size: {}".format(total_size))

    for status_code in sorted(status_codes):
        count = status_codes[status_code]
        print("{}: {}".format(status_code, count))
