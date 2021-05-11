#!/usr/bin/python3
"""
     Rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ A four sided shape """

    def __init__(self, width, height):
        super().integer_validator("height", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
