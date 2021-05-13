#!/usr/bin/python3
""" Module for read_file """


def read_file(filename=""):
    """ Function to read and print a file """
    with open(filename) as f:
        print(f.read(), end="")
