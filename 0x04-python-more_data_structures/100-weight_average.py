#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return (0)
    d = sum(map(lambda i: i[1], my_list))
    return (0 if d == 0 else sum(map(lambda i: (i[0] * i[1]), my_list)) / d)
