#!/usr/bin/python3
"""
Module Name: 101-add_attribute

Module Description:
This module contains only one function

Module Functions:
- add_attribute

Module Attributes:
None

"""


def add_attribute(object: object, name: str, value: str):
    """
    This function adds a new attribute with the given name
    and value to the specified object's dictionary.

    Parameters:
    -------------
    object: An object to which the new attribute should be added.
    name: A string representing the name of the new attribute to be added.
    value: A string representing the value of the new attribute to be added.
    Return Value:
    This function does not return any value.

    Exceptions:
    -------------
    If the specified object is of type int, float, str, or bool,
    then a TypeError is raised.

    Example usage:
    ---------------
    >>> add_attribute = __import__("101-add_attribute").add_attribute
    >>> class MyClass:
    ...     def __init__(self):
    ...             self.my_attribute = "initial value"
    ...
    >>> obj = MyClass()
    >>> add_attribute(obj, "new_attribute", "new value")
    >>> obj.new_attribute
    'new value'
    >>> add_attribute(42, "new_attribute", "new value")
    Traceback (most recent call last):
        ...
    TypeError: can't add new attribute

    """

    if not isinstance(object, (int, float, str, bool)):
        object.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
