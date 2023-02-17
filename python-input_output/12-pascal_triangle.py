#!/usr/bin/python3

def pascal_triangle(n):
    """
    This function generates the Pascal's triangle for a given positive integer n.

    Args:
    -------
    n: A positive integer that represents the number of rows of the Pascal's triangle to be generated.
    
    Returns:
    ---------
    Returns a list of lists of integers representing the Pascal's triangle of n.
    If n is less than or equal to 0, the function returns an empty list.
    
    Examples:
    ----------
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascal_triangle(1)
    [[1]]
    >>> pascal_triangle(-2)
    []
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
