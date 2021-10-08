#!/usr/bin/python3

""" Module that defines a division in all the elements of a matrix """


def matrix_divided(matrix, div):
    """a division in all the elements of a matrix

    Args:
        matrix ([list]): [Matrix passed to process]
        div ([int, float]): [denominator to aply]

    Raises:
        TypeError: [if the matrix is not a list of lists or if rows
        does'n contain numbers ]
        TypeError: [Rows size Mismatch]
        ZeroDivisionError: [div is 0]
    """

    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(matrix) is not list or len(matrix) == 0 \
            or not all([type(row) == list for row in matrix]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all([type(el) in [int, float] for row in matrix for el in row]):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if any(list(map(lambda row: len(row) == 0, matrix))):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(list(map(lambda row: len(matrix[0]) == len(row), matrix))):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return[[(el / div).__round__(2) for el in row] for row in matrix]
