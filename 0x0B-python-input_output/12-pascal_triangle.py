#!/usr/bin/python3
""" Module for pascal_triangle """


def pascal_triangle(n):
    """ Iterator function to print a pascal triangle of size n """
    if n <= 0:
        return []
    current = [1]
    while len(current) < n:
        new = current + [1]
        for i in range(1, len(current)):
            new[i] = current[i - 1] + current[i]
        current = new
        yield current
