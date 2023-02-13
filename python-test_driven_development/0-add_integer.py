#!/usr/bin/python3
"""
Module Name: 0-add_integer

Module Description:
This module contains only one function

Module Functions:
- def add_integer(a, b=98) -> int:

Module Attributes:
- None
"""


def add_integer(a, b=98) -> int:
    """
    This function adds two numbers, a and b, and returns the sum.
    If a or b is not an integer or a float, a TypeError is raised.
    If the result of the addition is positive or negative infinity, 89 is returned.
    Otherwise, the sum is returned as an integer.

    Input:
    a: an integer or a float
    b: an integer or a float, default 98

    Output:
    result: the sum of a and b, as an integer.

    Exceptions Raised:
    TypeError: If a or b is not an integer or a float.
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
