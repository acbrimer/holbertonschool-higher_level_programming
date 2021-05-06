#!/usr/bin/python3
""" Module defines function to print square """


def print_square(size):
    """ Function prints a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size != 0:
        print("\n".join([("#" * size) for r in range(size)]))
