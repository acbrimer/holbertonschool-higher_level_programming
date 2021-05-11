#!/usr/bin/python3
""" Module for MyInt """


class MyInt(int):

    """ Rebelious int """
    def __new__(cls, i):
        return super(MyInt, cls).__new__(cls, i)

    def __eq__(self, other):
        return super(MyInt, self).__ne__(other)

    def __ne__(self, other):
        return super(MyInt, self).__eq__(other)
