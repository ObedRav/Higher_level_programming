#!/usr/bin/python3
"""
Module Name: 1-my_list

Module Description:
This module contains only one function

Module Classes:
- MyList

Module Attributes:
- None
"""


class MyList(list):
    """
    A subclass of the built-in list class that provides an additional
    method for printing the list in sorted order.

    The MyList class inherits all the methods and properties of
    the built-in list class. In addition, it provides a new
    method called 'print_sorted' that sorts the list in ascending
    order and prints it to the console.
    """
    def print_sorted(self):
        """
        Sort the list in ascending order and print it to the console.

        Example usage:
        >>> l = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        >>> l.print_sorted()
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        """
        print(sorted(self))
