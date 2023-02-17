#!/usr/bin/python3
"""
Module Name: 100-my_int

Module Description:
This module contains a class that inherits from
the built-in int class and overrides its
eq and ne methods.

Module Classes:

MyInt
Module Attributes:

None
"""


class MyInt(int):
    """
    A subclass of the built-in int class that
    overrides the eq and ne methods.

    The MyInt class inherits from the built-in int
    class and redefines the __eq__ and __ne__
    methods to invert their usual behavior.

    Methods:
    - __eq__(self, other: int) -> bool: Overrides
    the built-in int class's __eq__ method
    to invert its behavior.
    - __ne__(self, other: int) -> bool: Overrides the
    built-in int class's __ne__ method
    to invert its behavior.

    Example usage:
    >>> a = MyInt(5)
    >>> c = 5
    >>> d = 6
    >>> a == 6
    True
    >>> c == d
    False
    >>> c != d
    True
    """
    def __eq__(self, other: int) -> bool:
        """
        Overrides the built-in int class's __eq__
        method to invert its behavior.

        The __eq__ method checks whether the value
        of this MyInt object plus 0 is not equal
        to the other integer. This has the effect
        of inverting the usual behavior of the
        equality operator (==).

        Parameters:
        - other: An integer to compare with this MyInt object.

        Returns:
        - True if the value of this MyInt object plus 0
        is not equal to the other integer.
        - False otherwise.

        Example usage:
        >>> a = MyInt(5)
        >>> a == 4
        True
        """
        return self + 0 != other

    def __ne__(self, other: int) -> bool:
        """
        Overrides the built-in int class's __ne__
        method to invert its behavior.

        The __ne__ method checks whether the value
        of this MyInt object plus 0 is equal to
        the other integer. This has the effect
        of inverting the usual behavior of the
        inequality operator (!=).

        Parameters:
        - other: An integer to compare with this MyInt object.

        Returns:
        - True if the value of this MyInt object
        plus 0 is equal to the other integer.
        - False otherwise.

        Example usage:
        >>> a = MyInt(5)
        >>> a != 6
        False
        """
        return self + 0 == other
