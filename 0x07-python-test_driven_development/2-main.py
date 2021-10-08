#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1.1, 4, 6],
    [8, 10, -12]
]
matrix_divided()
print(matrix_divided([1, 5, 6], 5))
print(matrix_divided([[1], [5, 6]], 5))
print(matrix)
