#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 != 0:
        letter = chr(letter - ord('a') + ord('A'))
    else:
        letter = chr(letter)
    print("{}".format(letter), end="")
