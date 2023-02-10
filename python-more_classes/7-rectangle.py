#!/usr/bin/python3
"""
Module Name: 0-rectangle

Module Description:
This module contains only one class

Module Classes:
- Rectangle

Module Attributes:
- None
"""


class Rectangle:
    """Empty class to represent a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0):
        # Vallidations
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value) -> None:
        # Vallidations
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        return self.__height * self.__width

    def perimeter(self) -> int:
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            symbol = str(self.print_symbol)
            return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self) -> None:
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
