#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    print("{0} argument{1}{2}".format(len(argv) - 1,
          ("s", "")[len(argv) == 2], (":", ".")[len(argv) == 1]))
    for ix, a in enumerate(argv[1:]):
        print("{0}: {1}".format(ix + 1, a))
