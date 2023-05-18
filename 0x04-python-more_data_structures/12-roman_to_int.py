#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    my_solution = 0
    old_val = 0
    for roman_letters in reversed(roman_string):
        value = roman_values.get(roman_letters, 0)

        if value >= old_val:
            my_solution += value
        else:
            my_solution -= value

        old_val = value
    return my_solution
