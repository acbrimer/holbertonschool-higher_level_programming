#!/usr/bin/python3
""" Module for inherits_from """


def inherits_from(obj, a_class):
    """ Checks if obj inherits from a_class """
    return isinstance(obj, a_class) and not type(obj) == a_class
