#!/usr/bin/python3
"""
This module contains functions to manipulate
matrices and check their properties.

Functions:
- `def lazy_matrix_mul(m_a, m_b)``

Modules Imported:
- NumPy

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function calculates the product of two matrices, m_a and m_b,
    using NumPy's np.matmul function.
    It assumes that the input matrices are valid and will not perform
    any checks to ensure they are.

    Input:
    m_a: list of lists of integers or floats
    m_b: list of lists of integers or floats

    Output:
    new_matrix: The product of m_a and m_b, as a NumPy array.

    Example:
    >>> a = np.array([[1, 2], [3, 4]])
    >>> b = np.array([[2, 0], [1, 2]])
    >>> lazy_matrix_mul(a, b) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS +REPORT_NDIFF
    array([[ 4, 4],
           [10,  8]])

    """
    new_matrix = np.matmul(m_a, m_b)
    return new_matrix
