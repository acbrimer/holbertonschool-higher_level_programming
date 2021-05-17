#!/usr/bin/python3
"""
    Module for the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """ Inherits from Rectangle with width = height """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def update(self, *args, **kwargs):
        """ Calls update on rectangle with width/height set to size """
        if len(args) != 0:
            superargs = list(args)
            if len(args) > 1:
                setattr(self, "size", args[1])
                superargs.insert(1, args[1])
            super().update(*superargs)
        else:
            superargs = dict(kwargs)
            if "size" in kwargs:
                setattr(self, "size", kwargs["size"])
                superargs["width"] = kwargs["size"]
                superargs["height"] = kwargs["size"]
            super().update(**superargs)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        Rectangle.validate_width_height("width", value)
        self.__size = value

    def __str__(self):
        return super().__str__().split("-")[0] + "- {}".format(self.__size)
