#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (number % 10) * (1, -1)[number <= 0]
print_str = "Last digit of {0} is {1} and is".format(number, last_digit)
if last_digit == 0:
    print("{} zero".format(print_str))
else:
    print(
        "{0} {1}".format(
            print_str,
            ("greater than 5", "less than 6 and not 0")[last_digit <= 5]
        )
    )
