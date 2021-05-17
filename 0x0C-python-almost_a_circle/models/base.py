#!/usr/bin/python3
"""
    Module for Base class
"""
import json


class Base:

    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a python list to JSON """
        return json.dumps(list_dictionaries)
