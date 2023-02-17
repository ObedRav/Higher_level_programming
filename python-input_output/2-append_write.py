#!/usr/bin/python3
"""
Module Name: 2-append_write

Module Description:
This module contains only one function

Module Classes:
- append_write

Module Attributes:
- None
"""


def append_write(filename="", text=""):
    """
    The append_write function appends the text specified by the
    text parameter to a file specified by the filename parameter.

    Parameters
    ------------
    filename (optional) : A string that represents the path to the file to be written. If no filename is provided, an empty string will be used as a default value.
    text (optional) : A string that represents the text to be appended to the file. If no text is provided, an empty string will be used as a default value.
    
    Returns
    ---------
    An integer that represents the number of characters appended to the file.

    Exceptions
    ------------
    PermissionError: If the specified file cannot be opened for writing.
    TypeError: If the text parameter is not a string.

    Tests
    --------
    >>> append_write("example.txt", "Hello")
    5
    >>> append_write("example.txt", " World")
    6
    >>> append_write("example.txt", "!")
    1
    >>> append_write("example.txt", "") # Test with empty string
    0
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
