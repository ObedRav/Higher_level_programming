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


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of a specific class.

    Args:
    - obj: the object to check.
    - a_class: the class to compare the object against.

    Returns:
    - True if the object is an instance of a subclass of the class, False otherwise.

    Example usage:
    >>> class MyClass:
    ...     pass
    ...
    >>> class MySubclass(MyClass):
    ...     pass
    ...
    >>> obj = MySubclass()
    >>> inherits_from(obj, MyClass)
    True
    >>> inherits_from(obj, MySubclass)
    False
    """
    if type(obj) == a_class:
        return False
    elif isinstance(obj, a_class):
        return True
