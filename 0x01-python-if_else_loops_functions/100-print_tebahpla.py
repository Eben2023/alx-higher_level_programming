#!/usr/bin/python3
for letter in range(90, 64, -1):
    print("{:c}".format(letter + 32 * (letter % 2)), end="")
print()
