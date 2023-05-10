#!/usr/bin/python3
def pow(a, b):
    result = 1
    for i in range(abs(b)):
        result *= a
    return 1 / result if b < 0 else result
