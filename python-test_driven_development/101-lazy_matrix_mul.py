#!/usr/bin/python3
"""
This module contains functions to manipulate
matrices and check their properties.

Functions:
- `is_matrix(lst)`
- `is_the_same_size(lst)`
- `is_matrix_empty(matrix)`
- `is_matrix_of_numbers(matrix)`
- `def lazy_matrix_mul(m_a, m_b)``

Modules Imported:
- NumPy

"""

import numpy as np

def is_matrix(lst):
    """
    Checks if the input is a matrix (a list of lists)
    
    Examples:
    >>> is_matrix([[1, 2, 3], [4, 5, 6]])
    True
    >>> is_matrix([[1, 2, 3], [4, 5, 6], []])
    True
    >>> is_matrix([1, 2, 3])
    False
    >>> is_matrix([[]])
    True
    """
    if all(isinstance(i, list) for i in lst):
        return True


def is_the_same_size(lst):
    """
    Checks if all rows in the matrix have the same size
    
    Examples:
    >>> is_the_same_size([[1, 2, 3], [4, 5, 6]])
    True
    >>> is_the_same_size([[1, 2, 3], [4, 5, 6, 7]])
    False
    >>> is_the_same_size([[]])
    True
    """
    num_cols = len(lst[0])
    return all(len(i) == num_cols for i in lst)


def is_matrix_empty(matrix):
    """
    Checks if the matrix is empty (all rows are empty lists)
    
    Examples:
    >>> is_matrix_empty([[1, 2, 3], [4, 5, 6]])
    False
    >>> is_matrix_empty([[], []])
    True
    >>> is_matrix_empty([[]])
    True
    """
    return all(not row for row in matrix)


def is_matrix_of_numbers(matrix):
    """
    Checks if all elements in the matrix are either integers or floats
    
    Examples:
    >>> is_matrix_of_numbers([[1, 2, 3], [4, 5, 6]])
    True
    >>> is_matrix_of_numbers([[1, 2, 3], [4, 5, '6']])
    False
    >>> is_matrix_of_numbers([[]])
    True
    """
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True

def lazy_matrix_mul(m_a, m_b):
    """
    This function calculates the product of two matrices, m_a and m_b,
    using a lazy evaluation approach and NumPy's np.matmul function.
    It performs several checks on the input matrices to ensure
    they are valid matrices (a list of lists containing integers or floats,
    with all rows having the same length, and not empty)
    before performing the matrix multiplication.
    If the input matrices are not valid, it will
    raise various exceptions (TypeError or ValueError)
    to indicate the error.

    Input:
    m_a: list of lists of integers or floats
    m_b: list of lists of integers or floats

    Output:
    new_matrix: The product of m_a and m_b, as a NumPy array.

    Exceptions Raised:
    TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a matrix (a list of lists),
               or if each row of m_a or m_b is not of the same size, or if m_a or m_b contains
               elements that are not integers or floats.
    ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not is_matrix(m_a):
        raise ValueError("m_a must be a list of lists")
    if not is_matrix(m_b):
        raise ValueError("m_b must be a list of lists")
    if is_matrix_empty(m_a):
        raise ValueError("m_a can't be empty")
    if is_matrix_empty(m_b):
        raise ValueError("m_b can't be empty")
    if not is_matrix_of_numbers(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not is_matrix_of_numbers(m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not is_the_same_size(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not is_the_same_size(m_b):
        raise TypeError("each row of m_b must be of the same size")

    new_matrix = np.matmul(m_a, m_b)

    return new_matrix
