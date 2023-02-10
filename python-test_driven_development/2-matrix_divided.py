#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix by a number.

    Args:
    matrix (list of lists): A matrix of integers or floats
    div (int or float): The number to divide the matrix by

    Returns:
    list of lists: The resulting matrix after division

    Raises:
    TypeError: If `div` is not a number, or if the elements of `matrix` are not integers or floats
    ZeroDivisionError: If `div` is equal to 0
    TypeError: If not all rows in `matrix` have the same length

    Example:

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

    >>> matrix_divided([[1, 2], [3, 4], [5, 6]], 2)
    [[0.5, 1.0], [1.5, 2.0], [2.5, 3.0]]

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers or floats")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
