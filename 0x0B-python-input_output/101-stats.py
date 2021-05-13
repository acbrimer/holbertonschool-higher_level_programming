#!/usr/bin/python3
"""
    Module for stats function
"""

import sys
import time


def parse_stat(s):
    """ Returns parsed tuple with (ip, status, size) """
    return (s.split(" ")[0],
            int(s.split(" ")[-2]),
            int(s.split(" ")[-1][0:-1]))

def get_stats():
    """ Reads stdin and prints aggregates every 10 lines until ^C """
    i = 1
    log = []
    try:
        buff = ""
        while True:
            s = sys.stdin.read(1)
            buff += s
            if s == "\n":
                try:
                    log.append(parse_stat(buff))
                    i += 1
                except Exception:
                    pass
                buff = ""
            if i == 10:
                size = sum(map(lambda l: l[-1], log))
                print("File size: {}".format(size))
                for r in sorted(set(map(lambda l: l[-2], log))):
                    count = list(map(lambda l: l[-2], log)).count(r)
                    print("{}: {}".format(r, count))
                i = 1
    except KeyboardInterrupt:
        size = sum(map(lambda l: l[-1], log))
        print("File size: {}".format(size))
        for r in sorted(set(map(lambda l: l[-2], log))):
            count = list(map(lambda l: l[-2], log)).count(r)
            print("{}: {}".format(r, count))
        sys.stdout.flush()
        pass

if __name__ == "__main__":
    get_stats()
