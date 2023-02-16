#!/usr/bin/python3
"""
Module Name: 0-lookup

Module Description:
This module contains only one function

Module Functions:
- lookup

Module Attributes:
- None
"""

def lookup(obj):
    """
    Print a list of all the attributes and methods of the specified object.

    Parameters:
    -----------
    obj : object
        The object to inspect.

    Returns:
    --------
    None.

    This function uses the built-in `dir()` function to retrieve
    a list of all the attributes and methods of the specified object.
    The list is printed to the console for easy inspection.

    >>> class ExampleClass:
    ...     def __init__(self):
    ...         self.x = 1
    ...     def foo(self):
    ...         pass
    >>> e = ExampleClass()
    >>> lookup(e) #doctest: +NORMALIZE_WHITESPACE
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
    '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', 'foo', 'x']

    """
    print(dir(obj))
