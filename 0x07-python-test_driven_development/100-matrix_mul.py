#!/usr/bin/python3
"""Defining multiplication between matrix"""


from typing import Type


def is_rectangle(matrix):
    return not any([len(row) != len(matrix[0]) for row in matrix])


def matrix_mul(m_a, m_b):

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all([type(row) is list for row in m_a]):
        raise TypeError("m_a must be a list of lists")
    if not all([type(row) is list for row in m_b]):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any([type(el) not in [int, float] for row in m_a for el in row]):
        raise TypeError("m_a should contain only integers or floats")
    if any([type(el) not in [int, float] for row in m_b for el in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not is_rectangle(m_a) or not is_rectangle(m_b):
        raise TypeError(
            "each row of m_a must be of the same size or each row of m_b \
            must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*m_b)] for
            row in m_a]
