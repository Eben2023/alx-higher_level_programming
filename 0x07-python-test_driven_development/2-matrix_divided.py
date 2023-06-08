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

    # Check if matrix is not a list or an empty list
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if each element in the matrix is a list
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Create a flattened list of all elements in the matrix
    flattened = [num for row in matrix for num in row]

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in flattened):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

    return result
