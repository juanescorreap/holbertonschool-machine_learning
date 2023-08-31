#!/usr/bin/env python3
def matrix_shape(matrix):
    """Retunrns the shape of a matrix"""
    if type(matrix) is not list:
        return []
    if len(matrix) == 0:
        return []
    if type(matrix[0]) is not list:
        return[len(matrix)]
    return[len(matrix)] + matrix_shape(matrix[0])
