#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print("0")
    else:
        print("{}".format(sum(map(int, argv[1:]))))
