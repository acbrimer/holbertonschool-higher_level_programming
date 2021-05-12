#!/usr/bin/python3
""" Module for add attribute """


def add_attribute(self, name, value):
    """ add attribute function """

    if not hasattr(self, "__dict__"):
        raise TypeError("cant't add new attribute")
    self.__setattr__(name, value)
