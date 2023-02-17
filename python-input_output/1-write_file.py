#!/usr/bin/python3
"""
Module Name: 1-write_file

Module Description:
This module contains only one function

Module Classes:
- write_file

Module Attributes:
- None
"""


def write_file(filename="", text=""):
    """
    The write_file function writes the text specified by the
    text parameter to a file specified by the filename parameter.

    Parameters
    ------------
    filename (optional) : A string that represents the path to the
                          file to be written. If no filename is provided,
                          an empty string will be used as a default value.
    text (optional) : A string that represents the text to be written to the
                      file. If no text is provided, an empty string will be
                      used as a default value.

    Returns
    ---------
    An integer that represents the number of characters written to the file.

    Exceptions
    ------------
    PermissionError: If the specified file cannot be opened for writing.
    TypeError: If the text parameter is not a string.

    Tests
    --------
    >>> write_file = __import__("1-write_file").write_file
    >>> write_file("file.txt", "Hello World!")
    12
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
