#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter not in [ord('q'), ord('e')]:
        print("{:c}".format(letter), end="")
