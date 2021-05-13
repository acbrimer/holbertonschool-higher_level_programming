#!/usr/bin/python3
"""
    Module for student class
"""


class Student:

    """ Student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        d = self.__dict__
        if attrs is not None:
            return dict((k, d[k]) for k in d.keys() if k in attrs)
        return d
