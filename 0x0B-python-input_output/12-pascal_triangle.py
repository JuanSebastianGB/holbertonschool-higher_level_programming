#!/usr/bin/python3

""" Module of the pascal triangle """


def pascal_triangle(n):
    """ Function that generates the pascal triangle"""
    if n <= 0:
        return []

    matrix = [[1]]
    while len(matrix) < n:

        last_row = matrix[-1]  # last row inserted
        actual_row = [1]  # [1] in left
        [actual_row.append(last_row[i] + last_row[i + 1])
         for i in range(len(last_row) - 1)]
        actual_row.append(1)  # [1] in right

        matrix.append(actual_row)
    return matrix
