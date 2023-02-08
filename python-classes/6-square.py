#!/usr/bin/python3
""" This module is about define a square """


class Square:
    """ This is a class that have size as a private property and
        run vallidations to the arguments"""
    def __init__(self, size=0, position=(0,0)):
        """ Attributes: size (int): size of the square """
        if not isinstance(size, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        if size < 0:  # If size is negative
            raise ValueError("size must be >= 0")
        if isinstance(position, tuple) and len(position) == 2 and all(map(lambda x: isinstance(x, (float, int)), position)):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # If size is not an integer
            raise TypeError("size must be an integer")
        if value < 0:  # If size is negative
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(map(lambda x: isinstance(x, (float, int)), value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self) -> int:
        """Function to calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Function to print the hash depending the value of size
        and print spaces depending on the value of position"""
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
