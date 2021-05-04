#!/usr/bin/python3
""" Module containing class definition for Square """


class Square:

    """ Square class

        Attributes:
            size: the size of the square
    """
    pass

    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
