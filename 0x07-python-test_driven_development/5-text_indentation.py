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
    # Check if the text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0

    # Skip leading spaces
    while count < len(text) and text[count] == " ":
        count += 1

    while count < len(text):
        # Print the current character without a newline
        print(text[count], end="")

        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")

            count += 1

            # Skip consecutive spaces
            while count < len(text) and text[count] == " ":
                count += 1

            continue

        count += 1
