#!/usr/bin/python3
""" Module for lookup function """


def lookup(obj):
    """ Function to return list of attribs & methods in obj """
    return list(obj.__dict__)
