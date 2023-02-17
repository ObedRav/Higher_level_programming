#!/usr/bin/python3
"""
Module Name: 4-from_json_string

Module Description:
This module contains only one function

Module Classes:
- from_json_string

Module Attributes:
- None
"""
import json


def from_json_string(my_str):
    """Returns the object represented by a JSON string.

    Args:
        my_str: The JSON string to be converted to a Python object.

    Returns:
        A Python object represented by the input JSON string.
    """
    return json.loads(my_str)
