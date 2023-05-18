#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    mykeys = list(a_dictionary.keys())
    for a in mykeys:
        if a_dictionary[a] == value:
            del a_dictionary[a]
    return a_dictionary
