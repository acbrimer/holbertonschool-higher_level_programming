#!/usr/bin/python3
""" Module for append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Appends new string to file after specified string """
    filelines = []
    matches = []
    with open(filename, "r+") as f:
        for l in f.readlines():
            filelines.append(l)
            if search_string in l:
                filelines.append(new_string)

    with open(filename, "w") as f:
        f.write("".join(filelines))
