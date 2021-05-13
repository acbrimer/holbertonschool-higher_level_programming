#!/usr/bin/python3
"""
    Module for Stats class
"""
import sys


class Stats:
    """ Class for reading/aggregating stats from stdin """
    __counter = 0

    def __init__(self):
        self.total_size = 0
        self.status_counts = {
            str(k): 0 for k in [200, 301, 400, 401, 403, 404, 405, 500]}
        self.get_stdin()

    def get_stdin(self):
        for line in sys.stdin:
            if "^C" == line.rstrip():
                break
            if len(line) > 50:
                size = int(line.split(" ")[-1][:-1])
                status = line.split(" ")[-2]
                self.total_size += size
                self.status_counts[status] += 1
                self.__counter += 1
                if self.__counter == 10:
                    self.print_vals()
                    self.__counter = 0

    def print_vals(self):
        print("File size: {}".format(self.total_size))
        for k in sorted(self.status_counts.keys()):
            if self.status_counts[k] > 0:
                print("{}: {}".format(k, self.status_counts[k]))

    def __del__(self):
        self.print_vals()

if __name__ == "__main__":
    s = Stats()
