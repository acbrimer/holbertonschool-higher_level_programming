#!/usr/bin/python3
""" Module for MyList class """


class MyList(list):
    """ Class inherits from list """
    def print_sorted(self):
        print(sorted(self))
