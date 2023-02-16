#!/usr/bin/python3
"""
Module Name: 8-rectangle

Module Description:
This module contains only one function

Module Classes:
- Rectangle

Module Attributes:
- None
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width: int, height: int):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
