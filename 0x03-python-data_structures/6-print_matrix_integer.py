#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            print(
                "{:d}".format(matrix[r][c]),
                end=(" ",
                     "\n")[c == len(matrix[r]) - 1])
