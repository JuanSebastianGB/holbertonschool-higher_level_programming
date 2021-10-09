#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
matriza = [
    [1, 2, 3],
    [3, 4, 7],
    [8, 5, 0]
]
matrizb = [
    [1, 2, 4],
    [3, 4, 9],
    [10, -4, -9]
]
print(matrix_mul(matriza, matrizb))
