#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return {x: y for x, y in a_dictionary.items() if y != value}
