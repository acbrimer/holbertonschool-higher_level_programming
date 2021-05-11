#!/usr/bin/python3
""" Module for LockedClass"""

@property
def first_name(self):
    return self.__first_name

@first_name.setter
def first_name(self, value):
    self.__first_name = value

def lc_init(self, first_name=""):
    self.__first_name = first_name
    
def lc_setattr(self, key, value):
    if not key == "first_name":
        raise AttributeError( "'LockedClass' object has no attribute '{}'".format(key))
    first_name(value)
    
LockedClass = type("LockedClass", (str, ), {
    """ LockedClass-- only accepts first_name """
    "__init__": lc_init,
    "__setattr__": lc_setattr,
    "first_name": first_name
})
