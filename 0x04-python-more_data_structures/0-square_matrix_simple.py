#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None or len(matrix) == 0:
         return (matrix)
    return (list(map(lambda i: list(map(lambda ii: ii ** 2, i)), matrix)))
    
