#!/usr/bin/python3
"""
Module Name: 4-5-save_to_json_file

Module Description:
This module contains only one function

Module Classes:
- save_to_json_file

Module Attributes:
- None
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function receives an object and a filename,
    then it saves the object as a JSON string in the file.

    Args:
    - my_obj: the object to be saved as JSON string.
    - filename: the name of the file to save the JSON string.

    Returns:
    - The number of characters written to the file.

    Raises:
    - TypeError: If the object cannot be serialized to JSON.
    - IOError: If there is an error when writing to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
