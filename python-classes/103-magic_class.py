#!/usr/bin/python3
""" This module is about a MagicClass to a Squeare """


import math


class MagicClass:
    """ This class represents a magic class """
    def __init__(self, radius=0):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return self.__radius**2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
