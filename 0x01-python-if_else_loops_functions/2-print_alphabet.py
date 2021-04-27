#!/usr/bin/python3
ascii_arr = list(range(ord('a'), ord('z')))
print("{}".format("".join(map(chr, ascii_arr))), end="")
