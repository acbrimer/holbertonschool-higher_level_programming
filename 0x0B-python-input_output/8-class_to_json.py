#!/usr/bin/python3
""" Module for class_to_json """


def class_to_json(obj):
    """ Gets dict of class """
    return obj.__dict__
