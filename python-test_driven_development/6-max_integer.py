#!/usr/bin/python3
"""
Module Name: 6-max_integer

Module Description:
This module contains only one function

Module Functions:
- def max_integer(list=[]) -> int

Module Attributes:
- None
"""


def max_integer(list=[]) -> int:
    """
    This function returns the biggest integer of a list of integers.

    Args:
    list (list, optional): list of integers to be searched. Defaults to [].

    Returns:
    int: The biggest integer of the list. If the list is empty, returns None.

    Examples:
    >>> max_integer([1, 2, 3, 4])
    4
    >>> max_integer([-1, -2, -3, -4])
    -1
    >>> max_integer([])
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
