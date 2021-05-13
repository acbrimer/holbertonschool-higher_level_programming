#!/usr/bin/python3
""" Module for append_write """


def append_write(filename="", text=""):
    """ Function to write text to file """
    with open(filename, "a") as f:
        return f.write(text)
