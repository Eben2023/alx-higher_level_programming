#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        ValueError: If n is less than or equal to 0.
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
