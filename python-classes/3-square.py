#!/usr/bin/python3
""" This module is about define a square """


class Square:
    """ This is a class that have size as a private property and
        run vallidations to the arguments"""
    def __init__(self, size=0):
        """ Attributes: size (int): size of the square """
        if not isinstance(size, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:  # If size is negative
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self) -> int:
        """Function to calculate the area of the square"""
        return self.__size * self.__size
