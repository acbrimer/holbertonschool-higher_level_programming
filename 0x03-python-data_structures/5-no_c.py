#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for i in range(len(my_string)):
        if my_string[i] not in ['c', 'C']:
            newstr += my_string[i]
    return (newstr)
