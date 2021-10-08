#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1.1, 4, 6],
    [8, 10, -12]
]
print(matrix_divided([[1, 2, float('inf')], [1, 2, 3]], 5))
print(matrix_divided([[1, 2], [5, 6]], float('inf')))
print(matrix)
