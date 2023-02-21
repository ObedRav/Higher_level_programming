#!/usr/bin/python3
class Vehicle:
    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if (value <= 0):
            raise ValueError("value must be > 0")
        self.__weight = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (value <= 0):
            raise ValueError("value must be > 0")
        self.__height = value
