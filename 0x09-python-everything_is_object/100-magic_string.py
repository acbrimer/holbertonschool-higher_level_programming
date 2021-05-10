def magic_string():
    magic_string.counter += 1
    return(", ".join(["Holberton" for i in range(magic_string.counter)]))
magic_string.counter = 0
