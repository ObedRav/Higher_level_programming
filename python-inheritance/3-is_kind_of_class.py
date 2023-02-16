#!/usr/bin/python3
"""
Module Name: 2-is_same_class

Module Description:
This module contains only one function

Module Functions:
- is_same_class

Module Attributes:
- None
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a specific class or a subclass.

    Args:
    - obj: the object to check.
    - a_class: the class to compare the object against.

    Returns:
    - True if the object is an instance of the class or a subclass,
    False otherwise.

    Example usage:
    >>> class MyClass:
    ...     pass
    ...
    >>> class MySubclass(MyClass):
    ...     pass
    ...
    >>> obj = MySubclass()
    >>> is_kind_of_class(obj, MyClass)
    True
    >>> is_kind_of_class(obj, int)
    False
    """
    return True if isinstance(obj, a_class) else False
