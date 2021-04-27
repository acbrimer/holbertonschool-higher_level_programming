#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if argv[2] not in ops.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print(
            "{0} {1} {2} = {3}".format(argv[1],
                                       argv[2],
                                       argv[3],
                                       ops[argv[2]](int(argv[1]),
                                                    int(argv[3]))))
