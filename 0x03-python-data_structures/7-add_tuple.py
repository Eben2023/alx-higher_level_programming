#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupA = tuple_a + (0, 0)
    tupB = tuple_b + (0, 0)
    return (tupA[0] + tupB[0], tupA[1] + tupB[1])
