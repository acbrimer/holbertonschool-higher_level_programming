#!/usr/bin/python3
from inspect import getmembers, isfunction
import hidden_4
if __name__ == '__main__':
    for m in getmembers(hidden_4, isfunction):
        if m[0][0:2] != "__":
            print("{}".format(m[0]))
