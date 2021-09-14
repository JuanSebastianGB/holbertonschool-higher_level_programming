#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            print("{:d}".format(matrix[i][j]),
                  end=" " if j + 1 < len(row) else "")
        print("")
