#!/usr/bin/python3
def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    min_rowlen = min(map(lambda r: len(r), matrix))
    max_rowlen = max(map(lambda r: len(r), matrix))
    if min_rowlen != max_rowlen:
        raise TypeError("Each row of the matrix must have the same size")
    if len(list(filter(
        lambda n: not isinstance(n, (int, float)), sum(matrix, [])
    ))) > 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    return list(map(lambda r:
                    list(map(lambda n: round(float(n) / div, 2), r)), matrix))
