#!/usr/bin/python3

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
    "__init__": lc_init,
    "__setattr__": lc_setattr,
    "first_name": first_name
})
