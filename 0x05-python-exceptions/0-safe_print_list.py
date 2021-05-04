#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if len(my_list) == 0:
        return (0)
    if x == 0:
        print(my_list[0])
        return (0)
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            print()
            return (i)
    print()
    return (i + 1)
