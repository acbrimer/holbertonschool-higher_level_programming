#!/usr/bin/python3
"""
    Module for save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function to write text to file """
    with open(filename, "w") as f:
        return f.write(json.dumps(my_obj))
