#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for r in range(len(matrix)):
            if matrix[r] is not None:
                for c in range(len(matrix[r])):
                    print(
                        "{:d}".format(matrix[r][c]),
                        end=(" ",
                             "\n")[c == len(matrix[r]) - 1])
