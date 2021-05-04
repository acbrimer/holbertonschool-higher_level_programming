#!/usr/bin/python3
""" Module containing class definition for Square """


class Square:

    """ Square class

        Attributes:
            size: the size of the square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        print("\n".join(["".join(["#" for r in range(self.__size)])
                         for c in range(self.__size)]))

    def area(self):
        return self.__size ** 2
