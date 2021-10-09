#!/usr/bin/python3
""" Defines lazy_matrix_mul function"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ Return the result of mult. between 2 matrix """
    return numpy.matmul(m_a, m_b)
