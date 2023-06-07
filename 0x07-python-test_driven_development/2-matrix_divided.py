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
    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) for row in matrix):
        raise TypeError("The matrix must be a list of lists")

    if not matrix:
        raise TypeError("The matrix must not be empty")

    num_rows = len(matrix)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("All rows of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("The divisor must be a numeric value")

    if div == 0:
        raise ValueError("The divisor cannot be zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
