#!/usr/bin/python3
"""
Module Name: 6-load_from_json_file

Module Description:
This module contains only one function

Module Classes:
- load_from_json_file

Module Attributes:
- None
"""
import json


def load_from_json_file(filename):
    """
    Returns the Python object represented by a JSON file.

    Args:
        filename (str): The name of the file.

    Returns:
        The Python object represented by the JSON file.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the file is empty.

    """
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)
