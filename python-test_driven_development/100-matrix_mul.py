#!/usr/bin/python3
"""
This module contains functions to manipulate
matrices and check their properties.

Functions:
- `is_matrix(lst)`
- `is_the_same_size(lst)`
- `is_matrix_empty(matrix)`
- `is_matrix_of_numbers(matrix)`
- `matrix_mul(m_a, m_b)`

"""


def is_matrix(lst):
    """Checks if the input is a matrix (a list of lists)"""
    if all(isinstance(i, list) for i in lst):
        return True


def is_the_same_size(lst):
    """Checks if all rows in the matrix have the same size"""
    num_cols = len(lst[0])
    return all(len(i) == num_cols for i in lst)


def is_matrix_empty(matrix):
    """Checks if the matrix is empty (all rows are empty lists)"""
    return all(not row for row in matrix)


def is_matrix_of_numbers(matrix):
    """Checks if all elements in the matrix are either integers or floats"""
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                return False
    return True


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
    m_a (list of lists): The first matrix to be multiplied.
    m_b (list of lists): The second matrix to be multiplied.

    Returns:
    list of lists: The result of the multiplication of two matrices.

    Raises:
    TypeError: If m_a or m_b is not a list.
    ValueError: If m_a or m_b is not a matrix, empty,
                or not all elements are integers or floats.
    ValueError: If m_a and m_b can't be multiplied.

    Examples:
    >>> matrix_mul([[1, 2], [3, 4]], [[2, 0], [1, 2]])
    [[4, 4], [10, 8]]

    >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]

    >>> matrix_mul([[1, 2], [3, 4]], [[1], [1]])
    [[3], [7]]
    """
    # Vallidations
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

    # Calculate the columns and rows
    columns_a = len(m_a)
    rows_a = len(m_a[0])
    matrix_size_a = [columns_a, rows_a]

    columns_b = len(m_b)
    rows_b = len(m_b[0])
    matrix_size_b = [columns_b, rows_b]

    decisition = ""
    size_new_matrix = []

    # Check if AB is posible
    if matrix_size_a[1] == matrix_size_b[0]:
        decisition = "AB"
        size_new_matrix = [columns_a, rows_b]
    # Check if BA is posible
    elif matrix_size_b[1] == matrix_size_a[0]:
        decisition = "BA"
        size_new_matrix = [columns_b, rows_a]
    else:
        raise ValueError("m_a and m_b can't be multiplied")

    # Inicialize the matrix
    new_matrix_rows = size_new_matrix[0]
    new_matrix_columns = size_new_matrix[1]
    new_matrix = []
    for i in range(new_matrix_rows):
        row = [0 for _ in range(new_matrix_columns)]
        new_matrix.append(row)

    if decisition == "BA":
        matrix_mul = m_b
        matrix_mul_2 = m_a
    else:
        matrix_mul = m_a
        matrix_mul_2 = m_b

    # Mulitplication
    for i in range(len(matrix_mul)):
        for j in range(len(matrix_mul_2[0])):
            for k in range(len(matrix_mul_2)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
