#!/usr/bin/python3
for c in reversed(range(97, 123)):
    print("{}".format((chr(c), chr(c - 32))[c % 2 != 0]), end="")
