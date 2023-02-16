#!/usr/bin/python3
"""
Module Name: 5-base_geometry

Module Description:
This module contains only one function

Module Classes:
- BaseGeometry

Module Attributes:
- None
"""


class BaseGeometry:
    """
    A base class that provides a method for
    calculating the area of a geometry shape.

    The BaseGeometry class does not implement the
    area() method. Instead, it raises an exception
    when called, to indicate that the method needs
    to be implemented by any subclass.

    Example usage:
    >>> class Rectangle(BaseGeometry):
    ...     def __init__(self, width, height):
    ...         self.width = width
    ...         self.height = height
    ...
    ...     def area(self):
    ...         return self.width * self.height
    ...
    >>> r = Rectangle(3, 4)
    >>> r.area()
    12
    """

    def area(self):
        """
        Raises an exception to indicate that the method is not implemented.

        Example usage:
        >>> g = BaseGeometry()
        >>> g.area()
        Traceback (most recent call last):
          ...
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
