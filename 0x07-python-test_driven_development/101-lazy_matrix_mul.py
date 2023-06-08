#!/usr/bin/python3

import numpy as np

"""Matrix Multiplication Module using NumPy."""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): List of lists representing the first matrix.
        m_b (list): List of lists representing the second matrix.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.

    Raises:
        ValueError: If the matrices' dimensions are incompatible
        for multiplication.

    Examples:
        >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        array([[ 7, 10],
               [15, 22]])
        >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        array([[13, 16]])
    """

    return (np.matmul(m_a, m_b))
