#!/usr/bin/python3
ascii_arr = list(range(ord('a'), ord('z')))
abc_str = "".join(map(chr, ascii_arr))
print(abc_str, end="")
