#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
	print("{} is zero")
else:
	print("{0} is {1}".format(number, ("positive", "negative")[number < 0]))
