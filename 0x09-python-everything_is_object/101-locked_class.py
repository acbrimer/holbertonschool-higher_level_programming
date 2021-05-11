#!/usr/bin/python3
""" Module for LockedClass"""

class LockedClass:
    """ LockedClass """
    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    def __init__(self, first_name=""):
        self.__first_name = first_name

    def __setattr__(self, key, value):
        if not key == "first_name":
            raise AttributeError( "'LockedClass' object has no attribute '{}'".format(key))
        self.first_name = value
