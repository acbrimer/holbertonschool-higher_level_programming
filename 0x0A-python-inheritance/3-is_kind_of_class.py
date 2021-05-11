#!/usr/bin/python3
""" Module for is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Checks if obj is kind of a_class """
    return a_class == object or a_class == type(obj)
