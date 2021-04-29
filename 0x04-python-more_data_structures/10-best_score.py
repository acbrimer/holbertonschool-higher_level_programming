#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not bool(a_dictionary):
        return None
    return (
        sorted(a_dictionary.items(), reverse=True, key=lambda i: i[1])[0][0])
