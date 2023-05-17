#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiply_lambda = lambda i: i * number
    result = list(map(multiply_lambda, my_list))
    return result
