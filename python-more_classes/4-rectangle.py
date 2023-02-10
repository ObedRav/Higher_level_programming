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

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Vallidations
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
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
        return "\n".join("".join("#" for _ in range(self.__width)) for _ in range(self.__height))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"
