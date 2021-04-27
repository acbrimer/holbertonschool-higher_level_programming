#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    a = 10
    b = 5
    for op in [["+", add], ["-", sub], ["*", mul], ["/", div]]:
        print("{0} {1} {2} = {3}".format(a, op[0], b, op[1](a, b)))
