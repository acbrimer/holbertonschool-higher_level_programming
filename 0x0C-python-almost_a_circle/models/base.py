#!/usr/bin/python3
"""
    Module for Base class
"""
import json
import os
import csv
import collections


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
    def create(cls, **dictionary):
        """ Creates a class list of specific type """
        return cls(**dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves JSON class list to file """
        filename = "{}.json".format(cls.__name__)
        filetext = list(
            map(lambda o: o.to_dictionary(),
                list_objs)) if list_objs is not None else []
        with open(filename, "w") as f:
            f.write(Base.to_json_string(filetext))

    @classmethod
    def load_from_file(cls):
        cls_json = None
        new_classes = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                cls_txt = f.read()
                cls_json = Base.from_json_string(cls_txt)
            for c in cls_json:
                new_c = cls.create(**c)
                new_classes.append(new_c)
            return list(new_classes)
        except Exception:
            return new_classes

    @classmethod
    def save_to_file_csv(cls, list_objs):
        d = list(map(lambda o: o.to_dictionary(), list_objs))
        with open("{}.csv".format(cls.__name__), "w") as f:
            writer = csv.DictWriter(f, fieldnames=d[0].keys())
            writer.writeheader()
            for data in d:
                o = {}
                for i in writer.fieldnames:
                    o[i] = data[i]
                writer.writerow(o)

    @classmethod
    def load_from_file_csv(cls):
        with open("{}.csv".format(cls.__name__)) as f:
            reader = csv.DictReader(f)
            dictobj = next(reader)
            return dictobj
