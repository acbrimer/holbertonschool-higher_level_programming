#!/usr/bin/python3
"""
    Module for load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ Function to load object from json in file """
    with open(filename) as f:
        return json.loads(f.read())
