#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    t = ".\n\n".join(map(lambda s: s.lstrip(), text.split(".")))
    t = ":\n\n".join(map(lambda s: s.lstrip(), t.split(":")))
    t = "?\n\n".join(map(lambda s: s.lstrip(), t.split("?")))
    print(t, end="")
