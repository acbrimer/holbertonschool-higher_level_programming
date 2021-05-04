#!/usr/bin/python3
""" Module containing class definition for Square """


class Square:

    """ Square class

        Attributes:
            size: the size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not (isinstance(position, tuple) and
                len(position) == 2 and
                isinstance(position[1], int) and
                isinstance(position[0], int) and
                min(position) >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[1], int) and
                isinstance(value[0], int) and
                min(value) >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        for y in range(self.__position[1]):
            print()
        print(
            "\n".join(
                [(" " * self.__position[0]) + "#" * self.__size
                 for c in range(self.__size)]))

    def area(self):
        return self.__size ** 2
