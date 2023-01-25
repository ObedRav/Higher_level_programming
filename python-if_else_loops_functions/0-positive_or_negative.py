#!/usr/bin/python3
import random


def checknumber(number):
    if (number < 0):
        print(f"{number} is negative")
    elif (number == 0):
        print(f"{number} is zero")
    else:
        print(f"{number} is positive")


number = random.randint(-10, 10)
checknumber(number)
