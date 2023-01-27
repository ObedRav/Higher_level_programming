#!/usr/bin/python3
def magic_calculation(a, b, c):
    if b < c:
        return a + b
    elif b > a:
        return c
    else:
        return a * b - c
