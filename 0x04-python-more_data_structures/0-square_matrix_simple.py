#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    return [[el[0]**2, el[1]**2, el[2]**2] for el in matrix]
