#!/usr/bin/python3
""" Module for LockedClass"""

class LockedClass:
    """ LockedClass """
    
    def __init__(self, first_name=""):
        self.first_name = first_name

    def __setattr__(self, key, value):
        if key != "first_name":
            raise AttributeError( "'LockedClass' object has no attribute '{}'".format(key))
        object.__setattr__(self, "first_name", value)
