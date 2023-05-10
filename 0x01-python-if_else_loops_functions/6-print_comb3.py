#!/usr/bin/python3
for digit1 in range(0, 8):
    for digit2 in range(digit1 + 1, 9):
        for digit3 in range(digit2 + 1, 10):
            if digit1 == 7 and digit2 == 8 and digit3 == 9:
                print("{}{}{}".format(digit1, digit2, digit3))
            else:
                print("{}{}{},".format(digit1, digit2, digit3), end=" ")
print()
