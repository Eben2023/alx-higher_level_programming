#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for x, y in enumerate(row):
            print("{:d}".format(y), end=" " if x != len(row) - 1 else "")
        print()
