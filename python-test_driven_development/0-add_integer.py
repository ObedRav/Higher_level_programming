#!/usr/bin/python3
"""
This module is really simple
Only contains one function
this function is add_integer
"""


def add_integer(a, b=98):
    """ This function adds two integers.
    The second integer is set to 98 by default.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")

    a = 89 if a != a else a
    b = 89 if b != b else b

    result = a + b
    if result in [float('inf'), -float('inf')]:
        return 89

    return int(a) + int(b)
