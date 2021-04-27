#!/usr/bin/python3
math = __import__('add_0', ['add'])
add = math.add
a = 1
b = 2
print("{0} + {1} = {2}".format(a, b, add(a, b)))
