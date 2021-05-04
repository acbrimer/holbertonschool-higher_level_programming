#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    if x == 0:
        return n
    for i in range(x):
        v = my_list[i]
        try:
            print("{:d}".format(v), end="")
            n += 1
        except:
            continue
    print()
    return n
