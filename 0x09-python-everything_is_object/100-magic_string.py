#!/usr/bin/python3
def magic_string():
    magic_string.c = (magic_string.c + 1 if 'c' in dir(magic_string) else 1) 
    return(", ".join(["Holberton" for i in range(magic_string.c)]))
