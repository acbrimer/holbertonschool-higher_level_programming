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
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Converts json string to object list """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves JSON class list to file """
        filename = "{}.json".format(cls.__name__)
        filetext = list(
            map(lambda o: o.to_dictionary(),
                list_objs)) if list_objs is not None else []
        with open(filename, "w") as f:
            f.write(Base.to_json_string(filetext))
