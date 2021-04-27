#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print(
            "{}".format(
                (c, chr(ord(c) - 32))[ord(c) >= 97 and ord(c) <= 124]
            ), end=""
        )
    print("")
