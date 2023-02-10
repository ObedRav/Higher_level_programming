#!/usr/bin/python3
"""
Module Name: 4-print_square

Module Description:
This module contains only one function

Module Functions:
- print_square(size) -> None

Module Attributes:
- None
"""


def print_square(size: int = 0) -> None:
    """
    This function takes in an integer `size`
    and printsa square of `#` characters
    with a side length of `size`.

    Parameters:
    size (int): The side length of the square to be printed.

    Returns:
    None

    Raises:
    TypeError: If `size` is not an integer.
    ValueError: If `size` is less than 0.

    Example:
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(0)
    >>> print_square(-2)
    Traceback (most recent call last):
    ValueError: size must be >= 0
    >>> print_square("4")
    Traceback (most recent call last):
    TypeError: size must be an integer
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()
