#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    new_matrix = []
    for i in range(matrix):
        for j in range(matrix[i]):
            new_matrix.append(matrix[i][j])
    return new_matrix
