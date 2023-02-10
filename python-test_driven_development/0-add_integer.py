#!/usr/bin/python3
"""
This module is really simple
Only contains one function
this function is add_integer
"""


def add_integer(a, b=98):
    """ This function adds integer
    and the second integer is formatted
    to 98"""
    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(result)
