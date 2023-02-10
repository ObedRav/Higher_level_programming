#!/usr/bin/python3
"""
Module Name: 3-say_my_name

Module Description:
This module contains only one function

Module Functions:
- say_my_name(first_name="", last_name="")

Module Attributes:
- None
"""


def say_my_name(first_name: str = "", last_name: str = "") -> None:
    """
    Prints the full name, given a first name and a last name.

    Parameters
    ----------
    first_name : str
        The first name of the person (default is "").
    last_name : str, optional
        The last name of the person (default is "").

    Raises
    ------
    TypeError
        If `first_name` is not a string.
    TypeError
        If `last_name` is not a string.

    Example
    -------
    >>> say_my_name("John", "Doe")
    My name is John Doe
    >>> say_my_name("Jane")
    My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
