#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
del my_rectangle

try:
    my_rectangle.width = 12
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))