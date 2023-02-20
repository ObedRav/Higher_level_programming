#!/usr/bin/python3
"""
Module Name: rectangle

Module Description:
This module contains only one Class

Module Classes:
- Rectangle

Module Attributes:
- None
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with dimensions and coordinates,
    which is a subclass of Base.

    Attributes:

    width: The width of the rectangle.
    height: The height of the rectangle.
    x: The x coordinate of the rectangle.
    y: The y coordinate of the rectangle.
    """
    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object with
        the given dimensions and coordinates.

        width: An integer representing the width of the rectangle.
        height: An integer representing the height of the rectangle.
        x: An integer representing the x coordinate of the rectangle.
           Default is 0.
        y: An integer representing the y coordinate of the rectangle.
           Default is 0.
        id: An integer representing the unique identifier of the rectangle.
            Default is None.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self) -> int:
            """Returns the value of the __width attribute"""
            return self.__width

    @width.setter
    def width(self, value: int):
            """Sets the value of the __width attribute"""
            self.__width = value

    @property
    def height(self) -> int:
            """Returns the value of the __height attribute"""
            return self.__height

    @height.setter
    def height(self, value: int):
            """Sets the value of the __height attribute"""
            self.__height = value

    @property
    def x(self) -> int:
            """Returns the value of the __x attribute"""
            return self.__x

    @x.setter
    def x(self, value: int):
            """Sets the value of the __x attribute"""
            self.__x = value

    @property
    def y(self) -> int:
            """Returns the value of the __y attribute"""
            return self.__y

    @y.setter
    def y(self, value: int):
            """Sets the value of the __y attribute"""
            self.__y = value
