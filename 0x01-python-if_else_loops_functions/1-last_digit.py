#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
digit = -digit

message = ["0" if digit == 0 else "less than 6 and not 0"
           if digit < 6 else "greater than 5"]
print(f"Last digit of {number} is {digit} and is {message[0]}")
