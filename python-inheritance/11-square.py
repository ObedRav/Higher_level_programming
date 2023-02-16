#!/usr/bin/python3
"""
Module Name: 10-square

Module Description:
This module contains the Square class,
which is a subclass ofthe Rectangle class.

Module Classes:
- Square

Module Attributes:
- None
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A subclass of the Rectangle class that represents a square.

    The Square class inherits from the Rectangle class and overrides
    the area() method to calculate the area of the square.

    Attributes:
    - __size: An integer representing the size of the square.

    Methods:
    - area(): Calculates the area of the square.
    - __str__(): Returns a string representation of the square.

    Example usage:
    >>> s = Square(5)
    >>> s.area()
    25
    >>> print(s)
    [Square] 5/5
    """

    def __init__(self, size: int):
        """
        Initializes a Square object with a specified size.

        The constructor uses the integer_validator method from the Rectangle
        class to validate the size argument.

        Parameters:
        - size: An integer representing the size of the square.

        Example usage:
        >>> s = Square(5)
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - The product of the size attribute squared.

        Example usage:
        >>> s = Square(5)
        >>> s.area()
        25
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - A string that represents the square in the format
        [Square] <size>/<size>

        Example usage:
        >>> s = Square(5)
        >>> print(s)
        [Square] 5/5
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
