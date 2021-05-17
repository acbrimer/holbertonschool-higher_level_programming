#!/usr/bin/python3
"""
    Module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):

    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_setter_value(attr, value):
        """ Validation checks for width, height, x, y attributes """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr))

    @staticmethod
    def validate_width_height(attr, value):
        """ Value checks for width and height attributes """
        Rectangle.validate_setter_value(attr, value)
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr))

    @staticmethod
    def validate_x_y(attr, value):
        """ Validation checks for x and y attributes """
        Rectangle.validate_setter_value(attr, value)
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr))

    def area(self):
        """ Returns the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Prints a representation of Rectangle using '#' """
        for i in range(self.y):
            print()
        print("\n".join(
            [" " * self.x + "#" * self.width for i in range(self.height)]))

    def update(self, *args, **kwargs):
        """ Update attributes in self from args """
        attrs = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for ix, arg in enumerate(args):
                if ix == len(attrs):
                    break
                setattr(self, attrs[ix], arg)
        else:
            for k in kwargs:
                if k in attrs:
                    setattr(self, k, kwargs[k])

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validate_width_height("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validate_width_height("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validate_x_y("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validate_x_y("y", value)
        self.__y = value

    def __str__(self):
        """ Override for string method """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id, self.x, self.y, self.width, self.height)
