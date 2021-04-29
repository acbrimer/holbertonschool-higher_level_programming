#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k in dict(
        filter(lambda i: i[1] == value, a_dictionary.items())
    ).keys():
        del a_dictionary[k]
    return (a_dictionary)
