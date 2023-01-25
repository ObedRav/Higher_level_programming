#!/usr/bin/python3
import random


def last_digit(number):
    last_digit = int(repr(number)[-1])
    return last_digit


number = random.randint(-10000, 10000)
print(f"Last digit of {number} is {last_digit(number)}", end=" ")
if (last_digit(number) == 0):
    print("and is 0")
elif (last_digit(number) < 6):
    print("and is less than 6 and not 0")
else:
    print("and is greater than 5")
