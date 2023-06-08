#!/usr/bin/python3
"""
This module defines text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']

    for char in text:
        print(char, end="")
        if char in punctuation_marks:
            print("\n\n", end="")
