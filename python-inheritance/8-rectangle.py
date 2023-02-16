#!/usr/bin/python3
"""
Module Name: 9-rectangle

Module Description:
This module contains only one function

Module Classes:
- Rectangle

Module Attributes:
- None
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass of the BaseGeometry class that represents a rectangle.

    The Rectangle class inherits from the BaseGeometry class and implements
    the area() method to calculate the area of the rectangle.

    Attributes:
    - __width: An integer representing the width of the rectangle.
    - __height: An integer representing the height of the rectangle.

    Methods:
    - area(): Calculates the area of the rectangle.
    - __str__(): Returns a string representation of the rectangle.

    Example usage:
    >>> r = Rectangle(3, 4)
    >>> r.area()
    12
    >>> print(r)
    [Rectangle] 3/4
    """

    def __init__(self, width: int, height: int):
        """
        Initializes a Rectangle object with a specified width and height.

        The constructor uses the integer_validator method from the BaseGeometry
        class to validate the width and height arguments.

        Parameters:
        - width: An integer representing the width of the rectangle.
        - height: An integer representing the height of the rectangle.

        Example usage:
        >>> r = Rectangle(3, 4)
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
