#!/usr/bin/python3
"""
     Square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ A shape with four equal sides """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
