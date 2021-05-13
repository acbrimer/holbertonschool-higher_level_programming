#!/usr/bin/python3
""" Module for write_file """


def write_file(filename="", text=""):
    """ Function to write text to file """
    with open(filename, "w") as f:
        return f.write(text)
