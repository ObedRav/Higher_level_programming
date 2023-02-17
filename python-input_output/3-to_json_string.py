#!/usr/bin/python3
"""
Module Name: 3-to_json_string

Module Description:
This module contains only one function

Module Classes:
- to_json_string

Module Attributes:
- None
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A string representing the JSON serialization of the input object.
    """
    return json.dumps(my_obj)
