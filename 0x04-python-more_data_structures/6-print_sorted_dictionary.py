#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _sorted = sorted(a_dictionary.keys())
    for key in _sorted:
        print("{}: {}".format(key, a_dictionary[key]))
