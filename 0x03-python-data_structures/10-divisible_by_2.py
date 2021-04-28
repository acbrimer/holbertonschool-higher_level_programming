#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    return (list(map(lambda i: i % 2 == 0, my_list)))
