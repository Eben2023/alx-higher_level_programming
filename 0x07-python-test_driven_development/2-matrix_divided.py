#!/usr/bin/python3
"""
Module doc for matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by `div`, rounded to
        2 decimal places.

    Raises:
        TypeError: If the `matrix` is not a list of lists of integers
        or floats,
            or if each row of the matrix does not have the same size.
        TypeError: If `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.

    """
    # Validate matrix input
    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    # Validate matrix rows size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div input
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
