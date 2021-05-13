#!/usr/bin/python3
""" Module for append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Appends new string to file after specified string """
    filelines = []
    matches = []
    with open(filename, "r+") as f:
        filelines = f.readlines()

    matches = [ix for ix, v in enumerate(filelines) if search_string in v]
    for m in matches:
        filelines.insert(m, new_string)

    with open(filename, "w") as f:
        f.write("".join(filelines))
