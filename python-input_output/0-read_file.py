#!/usr/bin/python3
"""
Module Name: 0-read_file

Module Description:
This module contains only one function

Module Classes:
- read_file

Module Attributes:
- None
"""


def read_file(filename="") -> None:
    """
    The read_file function reads and prints the contents of
    a file specified by the filename parameter.

    Parameters
    ------------
    filename (optional) : A string that represents the path
    to the file to be read. If no filename is provided,
    an empty string will be used as a default value.

    Returns
    ---------
    None

    Exceptions
    -----------
    FileNotFoundError: If the specified file does not exist or cannot be opened
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
        print(data, end="")
