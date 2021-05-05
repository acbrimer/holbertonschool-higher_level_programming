#!/usr/bin/python3
""" Module containing class definition for Rectangle """


class Rectangle:

    """ Rectangle class

        Attributes:
            width: width of rectangle
            height: height or rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return ((self.__width * 2) + (self.__height * 2), 0)[self.area() == 0]

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return (rect_1, rect_2)[rect_1.area() < rect_2.area()]

    def __str__(self):
        if self.area() == 0:
            return ""
        s = str(self.print_symbol)
        return "\n".join(
            [s * self.__width for r in range(self.__height)])

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        instance = cls(size, size)
        return instance
