#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return (None)
    return (list(map(lambda i: i * number, my_list)))
