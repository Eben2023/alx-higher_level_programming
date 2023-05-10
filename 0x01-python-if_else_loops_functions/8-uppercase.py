#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char_code = ord(c)
        if 97 <= char_code <= 122:
            char_code -= 32
        print("{:c}".format(char_code), end="")
    print()
