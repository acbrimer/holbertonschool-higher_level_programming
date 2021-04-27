#!/usr/bin/python3
import os
if __name__ == '__main__':
    s = str.encode("#pythoniscool\n")
    os.write(1, s)
