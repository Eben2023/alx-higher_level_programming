#!/usr/bin/python3

"""
Matrix Multiplication Module

This module provides a function for multiplying two matrices.

Functions:
    matrix_mul(m_a, m_b): Multiplies two matrices and
    returns the resulting matrix.

Module Usage:
    To use the matrix_mul function, import this module and call the
    function with two matrices as arguments.

Example:
    import matrix_mul

    result = matrix_mul.matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    print(result)  # Output: [[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): List of lists representing the first matrix.
        m_b (list): List of lists representing the second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or if the matrices
        can't be multiplied.
        TypeError: If any element of the matrices is not an integer or float.
        TypeError: If m_a or m_b is not a rectangle
        (rows have different sizes).

    Examples:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]
        >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13, 16]]
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or \
            not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b \
                        must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) \
        or not all(isinstance(num, (int, float))
                   for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats \
                        or m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or \
            any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or \
                        each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result
