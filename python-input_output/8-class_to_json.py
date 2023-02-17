#!/usr/bin/python3
"""
Module Name: 8-class_to_json

Module Description:
This module contains only one function

Module Classes:
- class_to_json

Module Attributes:
- None
"""


def class_to_json(obj):
    """
    The `class_to_json` function receives an object (obj) as input,
    which is an instance of a class. The function returns a dictionary
    representing the object's attributes that are serializable:
    list, dictionary, string, integer, and boolean. The dictionary
    is created by retrieving the `__dict__` attribute of the object,
    which contains all its attributes as key-value pairs.

    Input
    -------
    obj: an instance of a Class

    Output
    ________
    A dictionary representing the attributes of the input object that
    are serializable: list, dictionary, string, integer, and boolean.
    """
    return obj.__dict__
