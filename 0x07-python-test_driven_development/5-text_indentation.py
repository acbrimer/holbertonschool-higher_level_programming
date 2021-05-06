#!/usr/bin/python3
""" Module for text indentation function """


def text_indentation(text):
    """ Function breaks lines, left aligns between ?.: """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    t = ".\n\n".join(map(lambda s: s.lstrip(), text.split(".")))
    t = ":\n\n".join(map(lambda s: s.lstrip(), t.split(":")))
    t = "?\n\n".join(map(lambda s: s.lstrip(), t.split("?")))
    print(t, end="")
