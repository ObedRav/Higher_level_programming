#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
    - obj: the object to check.
    - a_class: the class to compare the object against.

    Returns:
    - True if the object is an instance of the class, False otherwise.

    Example usage:
    >>> class MyClass:
    ...     pass
    ...
    >>> obj = MyClass()
    >>> is_same_class(obj, MyClass)
    True
    >>> is_same_class(obj, int)
    False
    >>> num = 1
    >>> is_same_class(num, int)
    True
    >>> is_same_class(num, object)
    False
    """
    return True if type(obj) == a_class else False
