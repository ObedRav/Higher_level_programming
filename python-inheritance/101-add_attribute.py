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


def add_attribute(obj, name: str, value: str) -> None:
    """
    Adds a new attribute to an object if it's possible.

    Args:
    - obj: The object to add the attribute to.
    - name: The name of the attribute to add.
    - value: The value of the attribute to add.

    Raises:
    - TypeError: If the object can't have a new attribute.

    Returns:
    - None

    Example usage:
    >>> class MyClass():
    ...     pass
    ...
    >>> mc = MyClass()
    >>> add_attribute(mc, "name", "John")
    >>> print(mc.name)
    John
    >>> a = "My String"
    >>> add_attribute(a, "name", "Bob")
    Traceback (most recent call last):
    ...
    TypeError: can't add new attribute
    """
    if hasattr(obj, '__dict__') or (hasattr(type(obj), '__slots__') and name in type(obj).__slots__):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
