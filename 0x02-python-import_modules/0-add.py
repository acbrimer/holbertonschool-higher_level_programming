#!/usr/bin/python3
add = __import__('add_0', globals(), locals(), ['add'])
a = 1
b = 2
print("{0} + {1} = {2}".format(a, b, add.add(a, b)))
