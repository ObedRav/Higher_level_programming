#!/usr/bin/python3
"""
Module Name: 7-base_geometry

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

    def integer_validator(self, name:str, value:int):
        """
        Validates an integer value for a specific name parameter.
        It raises a TypeError if the value is not an integer,
        and a ValueError if the value is not greater than 0.

        Parameters:
        name: A string that represents the name of the parameter to validate.
        value: An integer that represents the value to validate.
        
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is not greater than 0.

        Example usage:
        >>> class Square(BaseGeometry):
        ...     def __init__(self, size):
        ...         self.integer_validator("size", size)
        ...         self.__size = size
        ...
        ...     def area(self):
        ...         return self.__size ** 2
        ...
        >>> s = Square(5)
        >>> s.area()
        25
        >>> s = Square(0)
        Traceback (most recent call last):
        ...
        ValueError: size must be greater than 0
        >>> s = Square('hello')
        Traceback (most recent call last):
        ...
        TypeError: size must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

